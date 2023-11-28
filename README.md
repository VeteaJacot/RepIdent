# RepIdent

RepIdent is a variant identity calculation program for any number of replicates of any number of samples in Variant Call Format (.vcf). RepIdent was developed as part of the HAI724I Teaching Unit at the Sciences faculty of Montpellier (see file "projet_replicatBio.pdf"). 

Usage : repident.sh [-h] [-p <folder path>] [-v <calculation mode>] 

where:

    -h : display this text

    -p : set path to the folder from which vcf files will be searched for (in a recursive way) for analysis (default = ~/)

    -v : set identity calculation mode (default = 3)
                
            - 1: count number of identical variants in all replicates for each position

            - 2: count number of identical variants in all replicates in a region of ten nucleotides around each position 

            - 3: compute mean identity of all variants in all replicates for each position
            
            
Example data is included for testing purposes ("Data" folder) and is property of [???]. The python and bash script files are distributed under a CC-by-sa Creative Commons licence.
