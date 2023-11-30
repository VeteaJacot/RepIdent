	# RepIdent

RepIdent is a variant identity calculation program for any number of replicates of any number of samples in Variant Call Format (.vcf). RepIdent was developed as part of the HAI724I Teaching Unit at the Sciences faculty of Montpellier (see file "projet_replicatBio.pdf", in french). 


Installation : 

		git clone https://github.com/VeteaJacot/RepIdent
		

Usage : 

	cd RepIdent-main/

	./repident.sh [-h] [-p <folder path>] [-v <calculation mode>] 

where

   -h : display this text

   -p : set path to the folder from which vcf files will be searched for (in a recursive way) for analysis (default = ~/)

   -v : set identity calculation mode (default = 3) (1: count number of identical variants in all replicates for each position ; 2: count number of identical variants in all replicates in a region of ten nucleotides around each position ; 3: compute mean identity of all variants in all replicates for each position)
         
            
Example data is included for testing purposes ("Data" folder) with no licence attached. The python and bash script files are distributed under an MIT licence.


Usage examples:

The included "Data" folder contains 3 replicate files for each of two samples. They are subsets of original VCF files for quick testing of RepIdent. Here are some examples of uses of the program using those files:

	- ./repident.sh -p [installation_folder]/RepIdent-main/Data/ -v 1

This will start the RepIdent script in version 1, which returns the number of identical variants at the same position for all replicates for each sample (P15 & P30), and start searching for VCF files to analyze in the provided "Data" folder. Expected result is
	
             "The replicates of the P30 sample have in total 2 identical variants
              The replicates of the P15 sample have in total 16 identical variants"
		 
	- ./repident.sh -p [installation_folder]/RepIdent-main/Data/ -v 2

This will start the RepIdent script in version 2, which returns the number of identical variants in a position range of 10 around the original position for all replicates for each sample (P15 & P30), and start searching for VCF files to analyze in the provided "Data" folder. Expected result is
	
             "The replicates of the P30 sample have in total 2 identical variants
              The replicates of the P15 sample have in total 18 identical variants"
		 
	- ./repident.sh -p [installation_folder]/RepIdent-main/Data/ -v 3

This will start the RepIdent script in version 2, which returns the identity percentage of variants at the same position for all replicates for each sample (P15 & P30), and start searching for VCF files to analyze in the provided "Data" folder. Expected result is
	
             "The replicates of the P30 sample show an identity of 06.6%
              The replicates of the P15 sample show an identity of 09.9%"

	- ./repident.sh -v 1

This will start the RepIdent script in version 1 and start searching in the default folder, which is the home folder of the current user (~/).

	
Notes:

This program expects VCF files to have names corresponding to the format " [sample name or number]-[replicate name or number][...].vcf ". VCF files can be placed anywhere inside the folder given as parameter, and VCF-like files (for example, vcf.stats files) can be present in the folder without affecting the program's function.

RepIdent does not consider the same <DEL> and <INS> values to be identical for two replicates. Two replicates with the value <DEL> at the same position 12345 will be considered to be two different variants for this position.

