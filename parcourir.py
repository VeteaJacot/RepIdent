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
# if a .vcf is encountered, the comp function of the compare.py script is called to add its information to the dicIdent dictionnary
# if a folder is encountered, the function calls itself to search in that folder

def browse(path, ver):

    
    for i in listdir(path):
        if isfile(join(path,i)):
            if i.split('.')[-1] == 'vcf':
                compare.comp(join(path,i), dicSamp, dicIdent, ver)
        if isdir(join(path,i)):
            browse(join(path,i), ver)
            
    return(dicIdent)


# final function to transform the dictionnary built by compare.py into an intepretable result dictionnary 
# the function then returns a one-line summary of each sample's replicates metric

def synth(dic, ver):
    
    if dic == {}:
        
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
    
    dicSamp = {}
    dicIdent = {}
    version = ["\"strict position variant count\"", "\"approximate position variant count\"", "\"strict position identity\""]
    
    print("\nProcess started for path \"" + sys.argv[1] + "\" in " + version[int(sys.argv[2])-1] + " version")
    
    print( synth( browse( sys.argv[1], sys.argv[2] ), sys.argv[2] ) + "\n")
            
    
        
            
    
                
