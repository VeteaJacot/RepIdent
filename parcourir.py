#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:52:07 2023

@author: vetea
"""

import sys
from os import listdir
from os.path import isfile, isdir, join, exists
import compare
    

# browsing function to recursively check if each file is a "variant call format" file or if it is a folder



def browse(path, ver):

    
    for i in listdir(path):
        
        if isfile(join(path,i)):
            
            if i.split('.')[-1] == 'vcf': # if a VCF file (.vcf extension) is encountered, the comp function of the compare.py script is called to add its information to the identity dictionnary (dicIdent)
                
                compare.comp(join(path,i), dicSamp, dicIdent, ver)
                
        if isdir(join(path,i)): # if a folder is encountered, the function calls itself to search in that folder
            
            browse(join(path,i), ver)
            
    return(dicIdent)


# final function to transform the dictionnary built by compare.py into an intepretable result dictionnary 
# the function then returns a one-line summary of each sample's replicates identity

def synth(dic, ver):
    
    if dic == {}: # return an error message in case no VCF files were found and the dictionary is empty
        
        res = "No VCF files were found in the specified folder : " + str(sys.argv[1]) + "\nCheck extensions and location of files you want to analyze"
        
    else:
    
        inc = 0
        count = 0
        ls = []
        
        for i in dic:
            
            if (ver == "1") or (ver == "2"):    # strict or approximate position variant count version
                
                for j in dic[i]:
                
                    count += dic[i][j]
                    
                ls.append(count)
                    
            if ver == "3":                      # strict position identity version
                
                for j in dic[i]:
                
                    if dic[i][j] >= 75.0:
                        count += 1
                    inc += 1
                
                ls.append(count/inc)
        
        inc = 0
        
        for i in dic:
            
            dic[i] = ls[inc]
            inc += 1
            
        res = ""
            
        if ver == "1":          # strict position variant count version
            
            for i in dic:
                
                res = res + "\nThe replicates of the " + str(i) + " sample have in total " + str(dic[i]) + " identical variants"
            
        elif ver == "2":        # approximate position variant count version
                
            for i in dic:
                    
                res = res + "\nThe replicates of the " + str(i) + " sample have in total " + str(dic[i]) + " identical variants (approximated position)"
                    
        else:                   # strict position identityt version
            
            for i in dic:
                
                res = res + "\nThe replicates of the " + str(i) + " sample show an identity of " + str(dic[i])[2:4] + "." + str(dic[i])[5] + "%"
        
    return(res)
    

# Main instructions : calling functions browse and synth to respectively build a dictionnary and create a summary of it 
# first, correct use of the program's parameters is checked

if not exists(str(sys.argv[1])):
    
    print("The folder path provided with '-p' (" + str(sys.argv[1]) + ") doesn't exist")

elif int(sys.argv[2]) not in [1,2,3]:
    
    print("The program version provided with '-v' (" + str(sys.argv[2]) + ") is invalid (valid values = 1, 2, or 3 ; see './repident.sh -h')")
    
else:
    
    dicSamp = {}    # initialisation of a dictionary structure to store encountered variant sequences
    dicIdent = {}   # initialisation of another dictionary structure to store computed identity values between replicates
    
    version = ["\"strict position variant count\"", "\"approximate position variant count\"", "\"strict position identity\""]
    
    print("\nProcess started for path \"" + sys.argv[1] + "\" in " + version[int(sys.argv[2])-1] + " version")
    
    dicRes = browse( sys.argv[1], sys.argv[2] )  # use of the browse function defined in this file to build the dicSamp et dicIdent structures from the files encountered
    
    if int(sys.argv[3]) == 1:  # if the user used the '-f' option, a file is generated, containing the raw dicIdent structure
        
        with open("Report.txt", 'w') as report:
            
            print(dicRes, file=report)
    
    print( synth( dicRes, sys.argv[2] ) + "\n")  # use of the synth function defined in this file to process results, which are then printed
     
    
        
            
    
                
