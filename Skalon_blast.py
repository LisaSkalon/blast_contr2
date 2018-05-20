from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import argparse


# парсинг - ввод инпута и аутпута (фаста)
def parse_inputs():
     parser = argparse.ArgumentParser(description='Blast search tool')
     parser.add_argument('-i', '--input' , help='Input file' , metavar='Str',
                    type=str, required=True)
     parser.add_argument('-o', '--output' , help='Output file' , metavar='Str',
                    type=str, required=True)
     
     args = parser.parse_args()
     return args.input, args.output

if __name__ == '__main__':
    in_file, out_file = parse_inputs()
#    Считываем инпут
    fasta = open(in_file).read()
#   Ищем в бласте первые совпадения всех последовательностей из инпута   
    result_handle = NCBIWWW.qblast("blastn", "nt", fasta, filter=True, hitlist_size=1, descriptions=1, alignments=1)
#   Записываем результат в xml файл, потом опять читаем его и парсим
    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    
    result_handle = open("my_blast.xml")
    blast_records = NCBIXML.parse(result_handle)
#   Достаем из xml только названия каждого организма из хита, запоминаем
    id_query=[]
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            id_query.append(alignment.hit_def)
    
#   Еще раз открываем инпут, чтобы считать содержимое       
    with open (in_file, 'r') as handle:
        records = list(SeqIO.parse(handle, "fasta"))
#   Формируем seqrecord, последовательностями служат последовательности из инпута,
#   заголовками - то, что мы гашли в бласте. Затем сортируем файл по заголовку,
#   таким образом одинаковые организмы окажутся рядом
    my_seqs=[]
    for i in range (len(id_query)):
        my_seqs.append(SeqRecord(Seq.Seq( str(records[i].seq), IUPAC.unambiguous_dna), id = id_query[i]))
    my_seqs_sort = sorted(my_seqs, key=lambda record : record.id)
#   Пишем результат в аутпут
    with open (out_file, "w") as handle: 
        SeqIO.write(my_seqs_sort, handle, 'fasta')   
        
        
    
        
        
        