#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:22:37 2021

@author: silicon
"""

import pymysql

def get_caled_inchikey(inchi_key):
    #print(inchi_key)
    #inchi_key = "RIVFGHBQSSJIRG-ZRDIBKRKSA-N"
    con=pymysql.connect(
    host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
    user='stx',     # 你的数据库用户名
    passwd='linux123',# 你的数据库密码
    db ='compound',
    charset='utf8')
    cursor=con.cursor()
    #execute执行一句查询语句
    sql ="SELECT count(inchi_key)  from conformation_table where inchi_key ='%s' "%inchi_key
    cursor.execute(sql)
    num = cursor.fetchone()[0]
    print("num",num)
    return num

def write_uncal_ele_frag(path,s):
    with open(path,'a') as f:
        f.write(s)

def read_inchi_key(path,path_1):
    inchi_key = []
    with open(path,'r') as f:
        lines = f.readlines()
    for line in lines:
        if len(line) >0:
            inchi = line.split(',')[0]
            #print('...',inchi,'....')
            num = 0
            try:
                num = get_caled_inchikey(inchi)
                #print(num)
            except:
                try:
                    num = get_caled_inchikey(inchi)
                except:
                    #num = 0
                    print(inchi, " is error to read")
                    continue
            if num == 0:
                s = line
                write_uncal_ele_frag(path_1,s)
                
if __name__ == '__main__':
    path = "/Users/silicon/python_script/statistic_num_qm_db/statistic_chem_space/ele_inchi_key_freq.csv"
    path_1 = "/Users/silicon/python_script/statistic_num_qm_db/statistic_chem_space/ele_inchi_uncal.log"
    read_inchi_key(path,path_1)
    
    
                
            
    
