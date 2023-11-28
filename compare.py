#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:52:32 2023

@author: vetea
"""

# Function for version 3 (strict position identity) of the script
# compares each newly-added sequence to each of the already-added sequences of the dictionnary and returns a mean of all sequences identities (identical bases / all bases)

def compIdent(list):
    
    ident = []
    
    for i in list:
        
        for j in (list[0:(list.index(i))]):
            
            match = 0
            count = 0
            
            for k in range(0 , min(len(i),len(j))):
                
                if i[k] == j[k]:
                    
                    match += 1
                    count += 1
                    
                else:
                    
                    count += 1
                           
            ident.append(( match / count ) * 100)
            
    if ident == []:
        
        return(100.0)
            
    else:

        return( sum(ident) / len(ident) )
            
           
# main function of compare.py ; for each line of the vcf file, adds the sequence to both sample dictionnary and identity dictionnary, and/or compares it to all already present sequences

def comp(path, dicSamp, dicIdent, ver):
    
    file_name = path.split('/')[-1]
    sample = file_name.split('-')[0]
    seq = []
    
    
    if sample not in dicSamp:
        
        dicSamp[sample] = {}
        dicIdent[sample] = {}
    
    file = open(path, "r")
    
    for l in file:
        if (l[0] != '#'):
            
            pos = l.split('\t')[1]
            seq = l.split('\t')[4]
            
            if ver == "1":          # strict position variant count version
                
                if dicSamp[sample] == {}:
                
                    dicPos = {pos : [seq]}
                    dicPosId = {pos : 0}
                    dicSamp[sample] = dicPos
                    dicIdent[sample] = dicPosId
        
                else:
                    
                    if pos in dicSamp[sample] :
                        
                        dicSamp[sample][pos].append(seq)
                        
                        for i in dicSamp[sample][pos][:-1]:
                            
                            if seq == i:
                                
                                dicIdent[sample][pos] += 1
                        
                    else:
                        
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0
                
                
            if ver == "2":          # approximate position variant count version
                
                if dicSamp[sample] == {}:
                
                    dicPos = {pos : [seq]}
                    dicPosId = {pos : 0}
                    dicSamp[sample] = dicPos
                    dicIdent[sample] = dicPosId
        
                else:
                    
                    if pos in dicSamp[sample]:
                        
                        dicSamp[sample][pos].append(seq)
                        
                        for i in dicSamp[sample][pos][:-1]:
                            
                            if seq == i:
                                
                                dicIdent[sample][pos] += 1
                    
                        for p in (range (int(pos)-10,int(pos)-1)):                            
                            
                            if str(p) in dicSamp[sample] :
                                
                                for i in dicSamp[sample][str(p)][:-1]:
                                    
                                    if seq == i:
                                        
                                        dicIdent[sample][pos] += 1
                                
                        for p in (range (int(pos)+1,int(pos)+10)):
                            
                            if str(p) in dicSamp[sample] :
                                
                                for i in dicSamp[sample][str(p)][:-1]:
                                    
                                    if seq == i:
                                        
                                        dicIdent[sample][pos] += 1
                            
                    else:
                            
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0
                        
                
            if ver == "3":          # strict position identity version
            
                if dicSamp[sample] == {}:
                
                    dicPos = {pos : [seq]}
                    dicSamp[sample] = dicPos
        
                else:
                    
                    if pos in dicSamp[sample] :
                        
                        dicSamp[sample][pos].append(seq)
                        dicIdent[sample][pos] = compIdent(dicSamp[sample][pos])
                        
                    else:
                        
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0.0
                    

    
                    
    file.close()
