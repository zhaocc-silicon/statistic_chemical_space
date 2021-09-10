#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:45:56 2021

@author: silicon
"""

import pymysql

def get_compond_info():
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT inchi_key from conformation_table where create_user= 'chengchengzhao'"
        cursor.execute(sql)
        moles = cursor.fetchall()
        return moles

def get_num_in_comp(inchi_key):   
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT count(inchi_key) from compound_table WHERE (inchi_key = '%s') " %inchi_key
        #print(sql)
        cursor.execute(sql)
        num=cursor.fetchone()[0]
        return num
    
if __name__ == '__main__':
    path = "mole_in_conf_not_in_comp_zcc.log"
    moles = get_compond_info()
    s =''
    num_moles = len(moles)
   # print(moles)
    for mole in moles:
        num = 0
        try:
            num = get_num_in_comp(mole[0])
        #print(num)
        except:
            try:
                num = get_num_in_comp(mole[0])
            except:
                print(mole[0] ," is error")
                continue
        if num ==0:
            s += mole[0] +'\n'
    with open(path,'w') as f:
        f.write("all_caled_moles: "+str(num_moles)+'\n')
        f.write(s)
            
        
        
        
        
        
        
        
        
        