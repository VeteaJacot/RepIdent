#!/bin/sh 


# help message displayed in case of wrong usage of the program call

help="\n--program to calculate replicate identity for any number of sample files in variant call format (.vcf)

Usage : $(basename "$0") [-h] [-p <folder path>] [-v <calculation mode>] [-f]

where:

    -h : display this text

    -p : set path to the folder from which vcf files will be searched for (in a recursive way) for analysis (default = ~/)

    -v : set identity calculation mode (default = 3)
                
            - 1: count number of identical variants in all replicates for each position

            - 2: count number of identical variants in all replicates in a region of ten nucleotides around each position 

            - 3: compute mean identity of all variants in all replicates for each position

    -f : write detailed results in 'report.txt' file

"

# default values of the program call variables

P=~/
V=3
F=0

# parsing of the command line call to get given parameters

while getopts ':v:p:fh' arg; do
  case "$arg" in
    h) echo "\n$help"
       exit
       ;;
    p) P=$OPTARG
       ;;
    v) V=$OPTARG
       ;;
    f) F=1
       ;;
    *) echo "\nillegal argument\n$help"
       exit
       ;;
  esac
done 

# in case no parameters are given, display the help message

if [ $# -eq 0 ];
then
   echo "\n$help"
   exit
fi

# python file call with given parameter variables

python3 parcourir.py $P $V $F
