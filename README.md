# Вторая контрольная работа по python

## Идентификация организмов с помощью blast

### Описание
Скрипт позволяет по данному фаста файлу искать организмы, которым принадлежат последовательности, и формирует на выходе новый файл с идентифицированными и отсортированными организмами

### Запуск

usage: Skalon_blast.py [-h] -i Str -o Str

Blast search tool

   arguments:  
  -h, --help            show this help message and exit  
  -i Str, --input Str   Input file  
  -o Str, --output Str  Output file  


### Пример использования

python3 Skalon_blast.py -i test_blast.fasta -o my_blast.fasta


Инпут:

\>?  
attgga  
\>??  
atggat  

Аутпут:

\>Hepatitis A virus isolate OHB-6, complete genome <unknown description>  
atggat  
\>Hepatitis B virus isolate OHBV-HIV006, complete genome <unknown description>  
attgga    
