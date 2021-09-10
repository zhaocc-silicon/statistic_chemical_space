#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:57:13 2021

@author: silicon
"""
import csv
from Read_DB import read_db as R_DB

ele_dict = {}
sec_dict = {}
rdb = R_DB()
def count_chembl_drugs():
   
    chemb_compound_inchi = []
    comp = rdb.get_chembl_drugs_compound()
    for com in comp:
        try:
            chemb_compound_inchi.append(com[0])                    
            ele_uniq, sec_uniq= rdb.get_compound_unique_key(com[0]) 
            if ele_uniq is not None:                                
                #print(ele_uniq)                                    
                ele_frags = rdb.get_comp_frag_inchi(ele_uniq)       
                for ele in ele_frags:                               
                    if ele[0] not in ele_dict.keys():               
                        ele_dict[ele[0]] = 1                        
                    else :                                          
                        ele_dict[ele[0]] += 1                       
            if sec_uniq != None :                                   
                sec_frags = rdb.get_comp_frag_inchi(sec_uniq)       
                for sec in sec_frags:                               
                    if sec[0] not in sec_dict.keys():               
                        sec_dict[sec[0]] = 1                        
                    else :                                          
                        sec_dict[sec[0]] += 1                              
        except:
            print("the compound error", com[0])
        
count_chembl_drugs()
#print(ele_dict)
#print(sec_dict)

ele_chain_frag = {}
ele_sing_ring_frag = {}
ele_double_ring_frag = {}
ele_triple_ring_frag = {}
ele_more_ring_frag = {}
for ele in ele_dict.keys():
    info = rdb.get_mole_info[ele]
    inchi_key, ring_number, heavy_atoms = info[0], info[1], info[2]
    if ring_number == 0 or ring_number == None:
        ele_chain_frag[inchi_key] = heavy_atoms
        
    
    
sec_chain_frag = []
sec_sing_ring_frag = []
sec_double_ring_frag = []

with open('chembl_ele_frag.csv', 'w') as f: 
    for key, value in ele_dict.items():
        f.write('{0},{1}\n'.format(key, value)) 

with open('chembl_sec_frag.csv', 'w') as f: 
    for key, value in sec_dict.items():
        f.write('{0},{1}\n'.format(key, value)) 
        
