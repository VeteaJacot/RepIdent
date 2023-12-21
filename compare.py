#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:52:32 2023

@author: vetea
"""

# Function for version 3 (strict position identity) of the script
# compares each newly-added sequence to each of the already-added sequences of the dictionnary and returns a mean of all sequences identities (identical bases / all bases)

def compIdent(lst):
    
    ident = []
    
    for i in lst:
        
        for j in (lst[0:(lst.index(i))]):
            
            match = 0
            count = 0
            
            for k in range(0 , min(len(i),len(j))):
                
                if i[k] == j[k]:
                    
                    match += 1
                    count += 1
                    
                else:
                    
                    count += 1
                           
            ident.append(( match / count ) * 100)
            
    if ident == []:  # in case no other sequence were found, total identity is initialised at 100%
        
        return(100.0)
            
    else:  # else, give the mean of all computed identities

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
                
                if dicSamp[sample] == {}: # if the sample is not already present in the sequences dictionary, an item is created for it
                
                    dicPos = {pos : [seq]}
                    dicPosId = {pos : 0}
                    dicSamp[sample] = dicPos
                    dicIdent[sample] = dicPosId
        
                else: 
                    
                    if pos in dicSamp[sample]:
                        
                        dicSamp[sample][pos].append(seq)
                        
                        for i in dicSamp[sample][pos][:-1]:
                            
                            if seq == i and seq != "<DEL>" and seq != "<DUP>":  # if a corresponding variant is found in the same position, the 'identity counter' is incremented by 1 ('DEL' and 'DUP' values are ignored) 
                                
                                dicIdent[sample][pos] += 1
                        
                    else:  # if the position is not already present in the corresponding sample item of the sequences dictionary, an item is created for it
                        
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0
                
                
            elif ver == "2":          # approximate position variant count version
                
                if dicSamp[sample] == {}:  # if the sample is not already present in the sequences dictionary, an item is created for it
                
                    dicPos = {pos : [seq]}
                    dicPosId = {pos : 0}
                    dicSamp[sample] = dicPos
                    dicIdent[sample] = dicPosId
        
                else:
                    
                    if pos in dicSamp[sample]:
                        
                        dicSamp[sample][pos].append(seq)
                        
                        # if a corresponding variant is found in the specified range, the 'identity counter' is incremented by 1 ('DEL' and 'DUP' values are ignored) 
                        
                        for i in dicSamp[sample][pos][:-1]:
                            
                            if seq == i and seq != "<DEL>" and seq != "<DUP>":
                                
                                dicIdent[sample][pos] += 1
                    
                        for p in (range (int(pos)-10,int(pos)-1)):   
                            
                            if str(p) in list(dicSamp[sample].keys()) :
                                
                                for i in dicSamp[sample][str(p)][:-1]:
                                    
                                    if seq == i and seq != "<DEL>" and seq != "<DUP>": 
                                        
                                        dicIdent[sample][pos] += 1
                                
                        for p in (range (int(pos)+1,int(pos)+10)):
                            
                            if str(p) in list(dicSamp[sample].keys()) :
                                
                                for i in dicSamp[sample][str(p)][:-1]:
                                    
                                    if seq == i and seq != "<DEL>" and seq != "<DUP>":
                                        
                                        dicIdent[sample][pos] += 1
                            
                    else:  # if the position is not already present in the corresponding sample item of the sequences dictionary, an item is created for it
                            
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0
                        
                
            elif ver == "3":          # strict position identity version
            
                if dicSamp[sample] == {}:  # if the sample is not already present in the sequences dictionary, an item is created for it
                
                    dicPos = {pos : [seq]}
                    dicSamp[sample] = dicPos
        
                else:
                    
                    if pos in dicSamp[sample] :
                        
                        dicSamp[sample][pos].append(seq)
                        
                        if seq != "<DEL>" and seq != "<INS>":
                        
                            dicIdent[sample][pos] = compIdent(dicSamp[sample][pos])  # if a corresponding variant is found in the specified range, the 'identity counter' is updated with the result of the comparison done by the compIdent function ('DEL' and 'DUP' values are ignored) 
                        
                    else:  # if the position is not already present in the corresponding sample item of the sequences dictionary, an item is created for it
                        
                        dicSamp[sample][pos] = [seq]
                        dicIdent[sample][pos] = 0.0
                    

    
                    
    file.close()
