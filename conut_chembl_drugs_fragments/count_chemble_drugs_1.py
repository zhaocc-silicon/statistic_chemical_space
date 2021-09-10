#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:57:13 2021

@author: silicon
"""
import csv
from Read_DB import read_db as R_DB
from plt_pic import plot_bar_pie
pp = plot_bar_pie()

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

def get_frag_ring_numbers(ele_dict):
    chain_frag = []
    sing_ring_frag = []
    double_ring_frag = []
    triple_ring_frag = []
    more_ring_frag = []
    
    for ele in ele_dict.keys():
        try:
            info = rdb.get_mole_info(ele)
            inchi_key, ring_number, heavy_atoms = info[0], info[1], info[2]
            if ring_number == 0 :
                chain_frag.append(heavy_atoms)
            elif ring_number == 1 :
               sing_ring_frag.append(heavy_atoms)
            elif ring_number == 2 :
                double_ring_frag.append(heavy_atoms)   
            elif ring_number == 3 :
                triple_ring_frag.append(heavy_atoms)
            else:
                more_ring_frag.append(heavy_atoms)
        except:
            print('get frag ring number rrror:',ele)
    info =  [len(chain_frag), len(sing_ring_frag), len(double_ring_frag), len(triple_ring_frag),len(more_ring_frag)]    
    print(info)
    return info


def freq_plt(ele_dict,task='ele'):   
              
    res = list(ele_dict.values()) 
    name_1 = ["chembl_ele_freq.csv","chembl_ele.jpg"]  
    name_2 = ["chembl_sec_freq.csv","chembl_sec.jpg"]  
   
    title = "elementary fragments vs themselves compounds number "
    name = name_1
    if task == 'sec':
        name = name_2
        title = "secondary fragments vs themselves compounds number "
       #print('i am sec')
   
       
    d_order = sorted(res,reverse=True)                                             
                                                                   
    title = title                                 
    picture_name = name[1]                                 
       #pp.plt_h_bar(x,y,title,picture_name) 
    dict_count = {'<10':0,'10-20':0,"20-30":0,'30-40':0,'40-50':0,">50":0}
    for y_i in d_order:
       if y_i < 10:
           dict_count['<10'] +=1
       elif y_i >= 10 and y_i <20:
           dict_count['10-20'] +=1
       elif y_i >= 20 and y_i <30:
           dict_count['20-30'] +=1
       elif y_i >= 30 and y_i <40:
           dict_count['30-40'] +=1
       elif y_i >= 40 and y_i <50:
           dict_count['40-50'] +=1
       else:
           dict_count['>50'] +=1
               
    x_1 = dict_count.keys()
    y_1 = dict_count.values()
    pp.plt_bar(x_1,y_1,title,picture_name)


print('ele_frag_ring_number:chain,ring,double-ring,trple_ring,more ')
ele_frag_ring_number = get_frag_ring_numbers(ele_dict)
print('sec_frag_ring_number:chain,ring,double-ring,trple_ring,more ')
sec_frag_ring_number = get_frag_ring_numbers(sec_dict)

freq_plt(ele_dict,task='ele')
freq_plt(sec_dict,task='sec')    


with open('chembl_ele_frag.csv', 'w') as f: 
    for key, value in ele_dict.items():
        f.write('{0},{1}\n'.format(key, value)) 

with open('chembl_sec_frag.csv', 'w') as f: 
    for key, value in sec_dict.items():
        f.write('{0},{1}\n'.format(key, value)) 
        
