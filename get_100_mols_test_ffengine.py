#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:33:08 2021

@author: silicon
"""

import pymysql

def get_ffengine_inchi():
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='forcefield',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT mole_inchi_key  from jobs WHERE job_type = 'intra'"
        cursor.execute(sql)
        moles = cursor.fetchall()
        return moles

def get_sec_frag_num(inchi):
    con=pymysql.connect(
    host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
    user='stx',     # 你的数据库用户名
    passwd='linux123',# 你的数据库密码
    db ='compound',
    charset='utf8')
    cursor=con.cursor()
    #execute执行一句查询语句
    sql ="SELECT uniq_key  from fragments_info WHERE inchi_key = '%s' and frag_level = 'secondary_fragment'"%inchi
    cursor.execute(sql) 
    uniq_key = cursor.fetchone()
    #print(uniq_key)
    if uniq_key != None:
        sql ="SELECT count(*)  from fragments_detail WHERE uniq_id = '%s'"%uniq_key[0]
        cursor.execute(sql)
        num = cursor.fetchone()[0]
    else:
        num = 0
    return num

def get_smile_from_comp(inchi):
    con=pymysql.connect(
    host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
    user='stx',     # 你的数据库用户名
    passwd='linux123',# 你的数据库密码
    db ='compound',
    charset='utf8')
    cursor=con.cursor()
    #execute执行一句查询语句
    sql ="SELECT smiles  from compound_table WHERE inchi_key = '%s'"%inchi
    cursor.execute(sql)
    smi = cursor.fetchone()[0]
    return smi

#print(get_ffengine_inchi())
#print(get_sec_frag_num("UTGQWJIIGZIEDP-UHFFFAOYSA-N"))
#print(get_smile_from_comp('XRLKRLRQZHZGFH-UHFFFAOYSA-N'))    
#exit
inchi_key_list = []
all_inchi = get_ffengine_inchi()
all_inchi = [i[0] for i in all_inchi]
all_inchi = list(set(all_inchi))
for inchi_key in all_inchi:
    if inchi_key != None:
        #print(inchi_key)
        num_sec = get_sec_frag_num(inchi_key)
        #print(num_sec)
        if  num_sec >= 2:
            smile = get_smile_from_comp(inchi_key)
            #print(inchi_key,smile)
            inchi_key_list.append([inchi_key,smile])
            if len(inchi_key_list)>100:
                break


with open("inchi_for_test_ffengine.log",'w') as f:
    for inchi in inchi_key_list:
        f.write("{}   {}\n".format(inchi[0],inchi[1]))
