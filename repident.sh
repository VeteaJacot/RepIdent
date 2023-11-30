#!/bin/sh 

help="\n--program to calculate replicate identity for any number of sample files in variant call format (.vcf)

Usage : $(basename "$0") [-h] [-p <folder path>] [-v <calculation mode>] 

where:

    -h : display this text

    -p : set path to the folder from which vcf files will be searched for (in a recursive way) for analysis (default = ~/)

    -v : set identity calculation mode (default = 3)
                
            - 1: count number of identical variants in all replicates for each position

            - 2: count number of identical variants in all replicates in a region of ten nucleotides around each position 

            - 3: compute mean identity of all variants in all replicates for each position

"

P=~/
V=3

while getopts ':v:p:h' arg; do
  case "$arg" in
    h) echo "\n$help"
       exit
       ;;
    p) P=$OPTARG
       ;;
    v) V=$OPTARG
       ;;
    *) echo "\nillegal argument\n$help"
       exit
       ;;
  esac
done


if [ $# -eq 0 ];
then
   echo "\n$help"
   exit
fi

#if test ! "$@"
#then
#    echo "\n$help"
#    exit
#fi


python3 parcourir.py $P $V
