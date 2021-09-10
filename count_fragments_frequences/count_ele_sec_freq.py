#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:18:52 2021

@author: silicon
"""

from Read_DB import read_db 
from collections import Counter
from plt_pic import plot_bar_pie
import csv
import sys

rd = read_db()
pp = plot_bar_pie()
mole_inchi_key = rd.get_compond_inchi()

#all_ele_inchi_1 = (('AAAAJHGLNDAXFP-VNKVACROSA-N',), ('AAAAKTROWFNLEP-UHFFFAOYSA-N',), 
#                  ('AAAATQFUBIBQIS-IRXDYDNUSA-N',), ('AAAAZQPHATYWOK-JXMROGBWSA-N',))

def count_eles(the_set):
    eles_list_0 = []
    eles_list_1 = []
    eles_list_2 = []
    eles_list_3 = []
    eles_list_more = []
    
    for ele in the_set:
        #print("the",ele)
        inchi_key = ele[0]
        num_ring = ele[1]
        try:
            num = rd.get_chembl_bb(inchi_key)    
        except:
            try:
                num = rd.get_mole_num_baba(inchi_key)  
                #num = rd.get_chembl_bb(inchi_key)
            except:
                print(inchi_key," does not get himself father")
                continue
        #if source == "ChEMBL_Drugs":
        #    pass
        #else:
       #     continue
        if num_ring ==0:
            eles_list_0.append((inchi_key,num))
        elif num_ring ==1:
            eles_list_1.append((inchi_key,num))
        elif num_ring ==2:
            eles_list_2.append((inchi_key,num))
        elif num_ring ==3:
            eles_list_3.append((inchi_key,num))
        else:
            eles_list_more.append((inchi_key,num))
            
    return [eles_list_0, eles_list_1, eles_list_2, eles_list_3, eles_list_more]          


def sort_plt(inchi_list,task='ele'):   
              
   res = count_eles(inchi_list)  
   name_1 = [["ele_chain_freq.csv","ele_chain.jpg"],["ele_single_freq.csv","ele_single.jpg"],
            ["ele_double_freq.csv","ele_double.jpg"],["ele_triple_freq.csv","ele_triple.jpg"],
            ["ele_more_freq.csv","ele_more.jpg"]]   
   name_2 = [["sec_chain_freq.csv","sec_chain.jpg"],["sec_single_freq.csv","sec_single.jpg"],
            ["sec_double_freq.csv","sec_double.jpg"],["sec_triple_freq.csv","sec_triple.jpg"],
            ["sec_more_freq.csv","sec_more.jpg"]] 
   
   title = "elementary fragments vs themselves compounds number "
   name = name_1
   if task == 'sec':
       name = name_2
       title = "secondary fragments vs themselves compounds number "
       #print('i am sec')
   for i in range(len(res)):
       res_i = res[i]
       if len(res_i)>0:
           pass
       else:
           continue
       file_name = name[i][0]
       pic_name = name[i][1]
       
       d_order = sorted(res_i,key=lambda x:x[1],reverse=True)           
       x = []                                                           
       y = []                                                          
                                                                   
       f = open(file_name,"w")                              
       csv_w = csv.writer(f)                                           
       for d_o in d_order:                                             
           x.append(d_o[0])                                            
           y.append(d_o[1])                                            
           csv_w.writerow([d_o[0],d_o[1]])                             
       f.close()                                                       
                                                                   
       title = title                                 
       picture_name = pic_name                                  
       #pp.plt_h_bar(x,y,title,picture_name) 
       dict_count = {'<1':0,'1-2':0,"2-3":0,'3-4':0,'4-5':0,'5-6':0,">6":0}
       for y_i in y:
           if y_i < 10:
               dict_count['<1'] +=1
           elif y_i >= 10 and y_i <100:
               dict_count['1-2'] +=1
           elif y_i >= 100 and y_i <1000:
               dict_count['2-3'] +=1
           elif y_i >= 1000 and y_i <10000:
               dict_count['3-4'] +=1
           elif y_i >= 10000 and y_i <100000:
               dict_count['4-5'] +=1
           elif y_i >= 100000 and y_i <1000000:
               dict_count['5-6'] +=1
           else:
               dict_count['>6'] +=1
               
       x_1 = dict_count.keys()
       y_1 = dict_count.values()
       pp.plt_bar(x_1,y_1,title,picture_name)
             
def get_frag_heavy_atoms_num(frag_level):
    sum_n = 0
    nums = rd.get_mol_heavy_atom_number(frag_level)   
    length = len(nums)
    if frag_level == 'sec':
        file_name = "sec_frag_heavy_num.csv"
        picture_name = 'sec_heavy_num.jpg'
        title = 'secondary_heavy_atomic_number'
    else:
        picture_name = 'ele_heavy_num.jpg'
        file_name = 'ele_frag_heavy_num.csv'
        title = 'elementary_heavy_atomic_number'
    f = open(file_name,'w')
    csv_w = csv.writer(f)
    dict_count = {'<10':0,'10-20':0,"20-30":0,'30-40':0,'40-50':0,'50-60':0,">60":0}
    for num in nums:
        sum_n += int(num[0])
        csv_w.writerow([int(num[0])])
        if int(num[0]) < 10:
            dict_count['<10'] +=1
        elif int(num[0]) >= 10 and int(num[0]) <20:
               dict_count['10-20'] +=1
        elif int(num[0]) >= 20 and int(num[0]) <30:
               dict_count['20-30'] +=1
        elif int(num[0]) >= 30 and int(num[0]) <40:
               dict_count['30-40'] +=1
        elif int(num[0]) >= 40 and int(num[0]) <50:
               dict_count['40-50'] +=1
        elif int(num[0]) >= 50 and int(num[0]) <60:
               dict_count['50-60'] +=1
        else:
               dict_count['>60'] +=1
    x_1 = dict_count.keys()
    y_1 = dict_count.values()
    pp.plt_bar_1(x_1,y_1,title,picture_name)
    
    print("number of fragments",length)
    print('sum',sum_n)
    print('average',sum_n/length)                   
                        
def get_calculated_molecules():
    pass
                                                                                                                           
if __name__ == "__main__":
    
    job_type = sys.argv[1]
    parameter = sys.argv[2]
    if job_type == 'freq':
        if parameter == 'ele':
            all_ele_inchi = rd.get_all_ele_frags_inchikey()
            sort_plt(all_ele_inchi,'ele') 
    
        elif parameter == 'sec':
            all_sec_inchi = rd.get_all_sec_frags_inchikey()
            sort_plt(all_sec_inchi,'sec') 
        else:
            print('you input an error parameter')
            sys.exit()
            
    elif job_type == 'atoms_num':
        if parameter == 'ele':
            get_frag_heavy_atoms_num(frag_level="ele")
        elif parameter == 'sec':
            get_frag_heavy_atoms_num(frag_level="sec")
        else:
            print('you input an error parameter')
            sys.exit()
    else:
        print('you input an error job_type')
        sys.exit() 
    
        
    
        









