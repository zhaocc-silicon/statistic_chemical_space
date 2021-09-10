#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:37:34 2020

@author: silicon
"""
import pymysql
#import os

class read_db():
    
    def __init__(self,inchi_key=""):
        self.inchi_key = inchi_key
    
    # give a inchi_key, get the  number of conformation
    def get_info(self,inchi_key):   
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source from compound_table WHERE (inchi_key = '%s') " %inchi_key
        #print(sql)
        cursor.execute(sql)
        try:
            num=cursor.fetchone()
            #num = list(num)
            #print(list(num))
        except:
            pass
        return num
    def get_compond_info(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source  from compound_table WHERE source != 'None'"
        cursor.execute(sql)
        moles = cursor.fetchall()[0:50]
        return moles
    def get_all_ele_frags(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source from compound_table WHERE frag_level = 'elementary_fragment' "
        cursor.execute(sql)
        #moles = cursor.fetchall()[0:50]
        moles = cursor.fetchall()
        return moles
    def get_caled_inchikey(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT inchi_key  from conformation_table"
        cursor.execute(sql)
        moles = cursor.fetchall()[0:50]
        return moles

    def get_compond_inchi(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT inchi_key  from compound_table WHERE source != 'None'"
        cursor.execute(sql)
        #moles = cursor.fetchall()[0:50]
        moles = cursor.fetchall()
        return moles 
    def get_mole_uniq_key(self,inchi_key):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT uniq_key from fragments_info WHERE inchi_key = '%s'"%inchi_key
        cursor.execute(sql)
        moles = cursor.fetchone()[0]
        return moles 
    
    def get_ele_frags_according_uniq_key(self,uniq_key):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT inchi_key  from fragments_detail WHERE uniq_id = '%s'"%uniq_key
        cursor.execute(sql)
        moles = cursor.fetchall()
        return moles   
    def get_all_ele_frags_inchikey(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT inchi_key, ring_number from compound_table WHERE frag_level = 'elementary_fragment' "
        cursor.execute(sql)
       # moles = cursor.fetchall()[0:50]
        moles = cursor.fetchall()
        return moles
    def get_all_sec_frags_inchikey(self):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT inchi_key, ring_number from compound_table WHERE frag_level = 'secondary_fragment' "
        cursor.execute(sql)
        #moles = cursor.fetchall()[0:50]
        moles = cursor.fetchall()
        return moles
    
    def get_mole_num_baba(self,inchi_key):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT count(DISTINCT uniq_id) from fragments_detail WHERE inchi_key = '%s'"%inchi_key
        cursor.execute(sql)
        num = cursor.fetchone()[0]
        print("num parents:",num)
        return num 
    def get_chembl_bb(self,inchi_key):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT DISTINCT uniq_id from fragments_detail WHERE inchi_key = '%s'"%inchi_key
        cursor.execute(sql)
        uniq_id = cursor.fetchall()
        bb_inchi_key = []
        for q_id in uniq_id:
            #print(q_id[0])
            sql = "SELECT inchi_key from fragments_info WHERE uniq_key = '%s'"%q_id[0]
            cursor.execute(sql)
            inchi_key = cursor.fetchone()[0]
            
            sql = "SELECT source from compound_table WHERE inchi_key = '%s'"%inchi_key
            cursor.execute(sql)
            source = cursor.fetchone()[0]
            if source == 'ChEMBL_Drugs':
                bb_inchi_key.append(inchi_key)
            
        print("chembl bb",len(bb_inchi_key))
        return  len(bb_inchi_key)
    def get_mol_heavy_atom_number(self,frag_level='secondary_fragment'):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT heavy_atoms from compound_table where frag_level = '%s'"%frag_level
        cursor.execute(sql)
        num = cursor.fetchall()
        #print("num bb",num)
        return num 
'''  
    def get_chembl(self, inchi_key):
        con=pymysql.connect(
        host='10.86.1.149',   # 连接你要取出数据库的ip，如果是本机可以不用写   
        user='stx',     # 你的数据库用户名
        passwd='linux123',# 你的数据库密码
        db ='compound',
        charset='utf8')
        cursor=con.cursor()
        #execute执行一句查询语句
        sql ="SELECT source from compound_table WHERE inchi_key = '%s'"%inchi_key
        cursor.execute(sql)
        num = cursor.fetchone()[0]
        print("num bb",num)
        return num 
'''
if __name__ == "__main__":
    rd = read_db()
    #rd.read_qm_num("MHUJOBBPKXYWKX-UHFFFAOYSA-N")
    #rd.read_num_local_min("MHUJOBBPKXYWKX-UHFFFAOYSA-N")
    #rd.read_num_conform("MHUJOBBPKXYWKX-UHFFFAOYSA-N")
    #rd.read_heavy_atoms_num_mass("MHUJOBBPKXYWKX-UHFFFAOYSA-N")
    #num = rd.get_info("DXGLGDHPHMLXJC-UHFFFAOYSA-N")
    #rd.read_num_conform("DXGLGDHPHMLXJC-UHFFFAOYSA-N")
    #rd.read_compound_ele_frag("2")
    #moles = rd.get_mole_uniq_key("AAAAJHGLNDAXFP-VNKVACROSA-N")
    #moles = rd.get_ele_frags_according_uniq_key("01707584fa0684f58b0bd2254eacc9c5")
    #num = rd.get_mole_num_baba("VNWKTOKETHGBQD-UHFFFAOYSA-N")
    #num = rd.get_all_ele_frags_inchikey()
    #num = rd.get_mol_heavy_atom_number()
    #num = rd.get_chembl("AAAAJHGLNDAXFP-VNKVACROSA-N")
    num = rd.get_chembl_bb("YJIRCOHLVHBXAK-UHFFFAOYSA-N")
    print(num)
    #print(num)
    
    
    
    
    
    