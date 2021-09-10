#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:07:29 2021

@author: silicon
"""
from Read_DB import read_db 

rd = read_db()

class get_inchi_key_from_db():
    
    def __init__(self):
        self.compound_info = []
        self.ele_info = []
        self.caled_info = []
    
    def get_compound(self):
        #inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source
        self.compound_info = rd.get_compond_info()       
    def get_all_frag(self):
        #inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source
        self.ele_info = rd.get_all_ele_frags()
    def get_caled_info(self):
        #self.caled_info = []
        inchi_keys = rd.get_caled_inchikey()
        for inchi in inchi_keys:
            self.caled_info.append(rd.get_info(inchi))
        
