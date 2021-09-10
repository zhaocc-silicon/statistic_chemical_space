


import os
import matplotlib.pyplot as plt
import numpy as np
from get_mol_info_rdkit import get_mol_attr
from read_moles_info import get_inchi_key_from_db
from plt_pic import plot_bar_pie
#heavy_atom = ["B","C","O","N","F","P","S","Cl","Br","Si","Se","As","I","Te"]
h_ele = ["H"]
normal_eles =["C","O","N","S","P"] 
halogen_eles = ["F","Cl","Br","I","At"]
f_metal_eles = ["Li","Na","K","Rb","Cs","Fe"]
s_metal_eles = ["Be","Mg","Ca","Sr","Ba","Ra"]
other_metal_eles_1 = ["Sc","Y","La","Ac","Ti","Zr","Hf","Rf","V","Nb","Ta","Db",\
                    "Cr","Mo","W","Sg","Mn","Tc","Re","Bh","Fe","Ru","Os","Hs",\
                    "Co","Rh","Ir","Mt","Ni","Pd","Pt","Ds","Cu","Ag","Au","Rg",\
                    "Zn","Cd","Hg","Cn","Al","Ga","In","Ti","Nh","Ge","Sn","Pb",\
                    "Fi","Sb","Bi","Mc","Po","Lv"]
other_metal_eles_2 = ["La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu",\
                      "Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr"]

other_non_metal_eles = ["B","Si","As","Se","Te"]
lazy_gas_ele = ["He","Ne","Ar","Kr","Xe","Rn","Og"]

metal_eles = f_metal_eles+s_metal_eles+other_metal_eles_1+other_metal_eles_2

all_eles =h_ele + normal_eles+halogen_eles+f_metal_eles+s_metal_eles+other_metal_eles_1+\
    other_metal_eles_2+other_non_metal_eles+lazy_gas_ele

heavy_eles = all_eles.copy()
heavy_eles.remove("H")

aromatic = ["ar1","ar2","ar3","ar4"]



class deal_data():
    
    def __init__(self):
        self.info = []
        self.all_eles_dict = {}
        self.all_halogen_eles_dict = {}
        self.all_non_metal_eles_dict = {}
        self.all_metal_eles_dict = {}
        
        self.ring_mole_num = 0
        self.chain_mole_num = 0
        
        self.coll_mass = []
        self.moles_num_atom = []
        self.ring_num_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,\
                              "8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,\
                             "15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"other":0}
        self.collect_ring_size = {"3":0,"4":0,"5":0,"6":0,"7":0,\
                              "8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,\
                             "15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"other":0}
        self.congj_ring_num = 0
        self.non_congj_ring_num = 0
        self.function_group_dict = {}
        self.fuse_ring_num = 0
        self.non_fuse_ring_num = 0
        self.aro_ring_num = 0
        self.non_aro_ring_num = 0
        #self.write_basic_info
    def  write_basic_info(self):
        s = 'molecule num:{}\n'.format(len(self.info))
        s += 'all elements number:\n'
        s1 = ''
        for ele, num in self.all_eles_dict.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
        
        s += 'all halogen number:\n'
        s1 = ''
        for ele, num in self.all_halogen_eles_dict.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
        
        s += 'all non-metal number:\n'
        s1 = ''
        for ele, num in self.all_non_metal_eles_dict.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
        
        s += 'all metal number:\n'
        s1 = ''
        for ele, num in self.all_metal_eles_dict.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
        
        s += 'all ring number:\n'
        s1 = ''
        for ele, num in self.ring_num_dict.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
        
        s += 'all ring size:\n'
        s1 = ''
        for ele, num in self.collect_ring_size.items():
            s1 += '{}:{} '.format(ele, num)
        s += s1
        s+='\n'
             
        s+= 'congj_ring_num: {}\n'.format(self.congj_ring_num)
        s+= 'non_congj_ring_num: {}\n'.format(self.non_congj_ring_num)
        s+= 'fuse_ring_num: {}\n'.format(self.fuse_ring_num)
        s+= 'non-fuse_ring_num: {}\n'.format(self.non_fuse_ring_num)
        s+= 'aro_ring_num: {}\n'.format(self.aro_ring_num)
        s+= 'non_aro_ring_num: {}\n'.format(self.non_aro_ring_num)
        with open ('basic_info.txt','w') as f:
            f.write(s)
    def get_compond_info(self):   #get moles info from compound_tab 
        g_key = get_inchi_key_from_db()
        g_key.get_compound()       
        ##inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source
        self.info = g_key.compound_info
        
    def get_ele_info(self):      # get ele_frags from compound_tab
        g_key = get_inchi_key_from_db()
        g_key.get_all_frag()
        self.info = g_key.ele_info

    def get_caled_info(self):   # get frags from conformation_tab & compound_tab
        g_key = get_inchi_key_from_db()
        g_key.get_caled_info()
        self.info = g_key.caled_info
        
    def count_info(self): 
        # a:inchi_key, smiles, function_group, ring_number, ring_size, ring_property, source
        for a in self.info:
            smiles = a[1]
            ring_property = a[5]
            #print(a[:3])
            if a[2] != None:
                function_group = a[2].split(",")  
            else:
                function_group = ''
                
            gma = get_mol_attr(smiles)
            #gma.get_eles()
            #gma.get_ring()
            #gma.cal_mass()            
            isring = gma.isring            # true or false
            num_ring = gma.num_ring          # int
            #is_congj=gma.congj_ring        # true or false
            ring_size = gma.ring_size         # [3,4]
            mass = gma.mass
            n_heavy_atoms = len(gma.heavy_atoms)
            self.moles_num_atom.append(n_heavy_atoms)
            #is_fuse_ring = gma.is_fuse_ring
            
            #heavy_atoms = gma.heavy_atoms
            all_atoms = list(set(gma.all_atoms))
            
            for ele in all_atoms:
                if ele in self.all_eles_dict:
                    self.all_eles_dict[ele] += 1   #统计元素分布
                else:
                    self.all_eles_dict[ele] =1
                    
                if ele in halogen_eles:
                    if ele in self.all_halogen_eles_dict:
                        self.all_halogen_eles_dict[ele] += 1
                    else:
                        self.all_halogen_eles_dict[ele] = 1
                if ele in other_non_metal_eles:
                    if ele in self.all_non_metal_eles_dict:
                        self.all_non_metal_eles_dict[ele] +=1
                    else:
                        self.all_non_metal_eles_dict[ele] =1
                if ele in metal_eles:
                    if ele in self.all_metal_eles_dict:
                        self.all_metal_eles_dict[ele] +=1
                    else:
                        self.all_metal_eles_dict[ele] = 1
                    
            self.coll_mass.append(mass)        #统计质量分布
            if isring:
                if ring_property != None:
                    ring_property = ring_property.split(",")
                    for pro in ring_property:
                        if pro in aromatic:
                            self.aro_ring_num +=1
                        else:
                            self.non_aro_ring_num +=1
                self.ring_mole_num +=1        #统计链状分子和环状分子数目
                if gma.congj_ring_num >0:     #以分子作为对象
                    self.congj_ring_num +=1    
                #self.congj_ring_num += gma.congj_ring_num
                if gma.non_congj_ring_num >0:
                    self.non_congj_ring_num +=1
                #self.non_congj_ring_num += gma.non_congj_ring_num
                if gma.fuse_ring_num >0:
                    self.fuse_ring_num += 1
                #self.fuse_ring_num += gma.fuse_ring_num
                if gma.non_fuse_ring_num >0:
                    self.non_fuse_ring_num  +=1
                #self.non_fuse_ring_num  += gma.non_fuse_ring_num
            else:
                self.chain_mole_num +=1
            if int(num_ring) <= 20:    
                self.ring_num_dict[str(num_ring)] +=1   #统计分子拥有的环的个数
            else:
                self.ring_num_dict["other"] +=1
            ring_size = list(set(ring_size))   
            if len(ring_size) >0:
                for size in ring_size:
                    #print(ring_size)
                    if size <= 20:
                        self.collect_ring_size[str(size)] +=1
                    else:
                        self.collect_ring_size["other"] +=1
            
            if len(function_group) >0:              #统计官能团
                for fg in function_group:
                    if fg in self.function_group_dict:
                        self.function_group_dict[fg] +=1
                    else:
                        self.function_group_dict[fg] = 1
            

class plt():

    def __init__(self):
        self.dd = deal_data()
        self.dd.get_compond_info() 
        #self.dd.get_ele_info()
        #self.dd.get_caled_info()   
        self.dd.count_info()
        self.dd.write_basic_info()
        self.pp = plot_bar_pie()
        
    def analyze_eles_type(self):
        all_eles_dict = self.dd.all_eles_dict #{'C': 29, 'N': 2, 'O': 9}
        all_halogen_eles_dict = self.dd.all_halogen_eles_dict
        all_non_metal_eles_dict = self.dd.all_non_metal_eles_dict
        all_metal_eles_dict = self.dd.all_metal_eles_dict
        
        eles = {"C":0,"H":0,"O":0,"N":0,"X":0,"metal":0,"nonmetal":0}
        for ele, num in all_eles_dict.items():
            if ele in eles:
                eles[ele] = num
        num = 0
        for hal,n in  all_halogen_eles_dict.items():
            num +=n
        eles["X"] =  num
        
        num = 0
        for metal, n in all_metal_eles_dict.items():
            num +=n
        eles["metal"] = num
        
        num = 0
        for non_m, n in all_metal_eles_dict.items():
            num += n
        eles["nonmetal"] = num
        
        labels = eles.keys()
        values = eles.values()
        title ="All Eles" 
        picture_name = "pie_chart_for_all_eles.jpg"
        #plt_pie(labels,value,explode = None,title, picture_name)
        #print(labels,values)
        self.pp.plt_pie(labels, values, None,title, picture_name)
        
        hal_labels = all_halogen_eles_dict.keys()
        hal_values = all_halogen_eles_dict.values()
        title ="Halogen Eles" 
        picture_name = "pie_chart_halgen_eles.jpg"
        self.pp.plt_pie(hal_labels, hal_values, None,title, picture_name)
        
        met_labels = all_metal_eles_dict.keys()
        met_values = all_metal_eles_dict.values()
        title ="Metal Eles" 
        picture_name = "pie_chart_metal_eles.jpg"
        self.pp.plt_pie(met_labels, met_values, None,title, picture_name)
        
        non_met_labels = all_non_metal_eles_dict.keys()
        non_met_values = all_non_metal_eles_dict.values()
        title ="Nonmetal Eles" 
        picture_name = "pie_chart_non_metal_eles.jpg"
        self.pp.plt_pie(non_met_labels, non_met_values, None,title, picture_name)
               
    def analyze_heavy_atom_number(self):
        moles_num_atom = self.dd.moles_num_atom
        #print(len(moles_num_atom))
        num_moles = {"0-10":0,"10-20":0,"20-30":0,"30-40":0,"40-":0}
        for num in moles_num_atom:
            if num > 40:
                num_moles["40-"] +=1
                continue
            if num >30:
                num_moles["30-40"] +=1
                continue
            if num >20:
                num_moles["20-30"] +=1
                continue
            if num >10:
                num_moles["10-20"] +=1
                continue
            else:
                num_moles["0-10"] +=1
        labels = num_moles.keys()
        values = num_moles.values()
        title ="Moles Number" 
        picture_name = "pie_chart_for_all_moles_number.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)
        
    def analyze_moles_weight(self):
        coll_mass =self.dd.coll_mass
        num_moles = {"0-100":0,"100-200":0,"200-300":0,"300-400":0,"400-":0}
        for num in coll_mass:
            if num > 400:
                num_moles["400-"] +=1
                continue
            if num >300:
                num_moles["300-400"] +=1
                continue
            if num >200:
                num_moles["200-300"] +=1
                continue
            if num >100:
                num_moles["100-200"] +=1
                continue
            else:
                num_moles["0-100"] +=1
        labels = num_moles.keys()
        values = num_moles.values()
        title ="Moles Mass" 
        picture_name = "pie_chart_for_all_moles_mass.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)
        
    def analyze_topological_structure(self):
        
        ring_mole_num = self.dd.ring_mole_num  # 3
        chain_mole_num = self.dd.chain_mole_num # 3
        
        ring_num_dict = self.dd.ring_num_dict #{'0': 3, '1': 2, '2': 0, '3': 0}
        collect_ring_size= self.dd.collect_ring_size #{'3': 0, '4': 0, '5': 1, '6': 1}
        
        congj_ring_num = self.dd.congj_ring_num # 2
        non_congj_ring_num = self.dd.non_congj_ring_num # 3
        
        aro_ring_num = self.dd.aro_ring_num  # 34
        non_aro_ring_num = self.dd.non_aro_ring_num #435
        
        fuse_ring_num = self.dd.fuse_ring_num
        non_fuse_ring_num = self.dd.fuse_ring_num
        
        ring_num = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,\
                              "8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,\
                             "15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"other":0}
        ring_size = {"3":0,"4":0,"5":0,"6":0,"7":0,\
                              "8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,\
                             "15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"other":0}
        
        labels = ["ring","chain"]
        values = [ring_mole_num,chain_mole_num]
        title ="ring chain" 
        picture_name = "pie_chart_for_ring-chain.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)
        #print(ring_num_dict)
        for key, value in ring_num_dict.items():
            if key in ring_num:
                ring_num[key] = value
                #print(ring_num)        
        x = ring_num.keys()
        y = ring_num.values()
        title ="ring num" 
        #print(x,y)
        picture_name = "pie_chart_for_ring_num.jpg"
        self.pp.plt_bar(x, y, title, picture_name)
        
        for key, value in collect_ring_size.items():
            if key in ring_size:
                ring_size[key] = value       
        x = ring_size.keys()
        y = ring_size.values()
        title ="ring size" 
        picture_name = "pie_chart_for_ring_size.jpg"
        self.pp.plt_bar(x, y, title, picture_name)
        
        labels = ["aro_ring","non_aro_ring"]
        values = [aro_ring_num,non_aro_ring_num]
        title ="aro ring" 
        picture_name = "pie_chart_for_aro-ring.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)
        
        labels = ["congj_ring","non_congj_ring"]
        values = [congj_ring_num,non_congj_ring_num]
        title ="congj ring" 
        picture_name = "pie_chart_for_congj-ring.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)
        
        labels = ["fuse_ring","non_fuse_ring"]
        values = [fuse_ring_num,non_fuse_ring_num]
        title ="fuse ring" 
        picture_name = "pie_chart_for_fuse-ring.jpg"
        self.pp.plt_pie(labels, values, None,title, picture_name)

    def analyze_functional_group(self):        
        function_group_dict = self.dd.function_group_dict # {'ke_am': 1, 'ke': 1, 'ene': 2}
        d_order = sorted(function_group_dict.items(),key=lambda x:x[1],reverse=False)
        x = []
        y = []
        for d_o in d_order:
            x.append(d_o[0])
            y.append(d_o[1])
        title = "function group"
        picture_name = "function_group.jpg"
        self.pp.plt_h_bar(x,y,title,picture_name)
        
        
if __name__ == "__main__":
    #dd = deal_data()
    #dd.get_caled_info()
    #dd.get_compond_info()
    #dd.get_ele_info()
    #dd.count_info()
    #print(len(dd.info))
    #print(dd.all_eles_dict)
    
    #all_eles_dict = dd.all_eles_dict #{'C': 29, 'N': 2, 'O': 9}
    #all_halogen_eles_dict = dd.all_halogen_eles_dict
    #all_non_metal_eles_dict = dd.all_non_metal_eles_dict
    #all_metal_eles_dict = dd.all_metal_eles_dict
    #moles_num_atom = dd.moles_num_atom
    #coll_mass =dd.coll_mass          # [155.15300000000008, 118.17599999999993, 122.18199999999995]
    #ring_mole_num = dd.ring_mole_num  # 3
    #chain_mole_num = dd.chain_mole_num # 3
    #ring_num_dict = dd.ring_num_dict #{'0': 3, '1': 2, '2': 0, '3': 0}
    #collect_ring_size= dd.collect_ring_size #{'3': 0, '4': 0, '5': 1, '6': 1}
    #congj_ring_num = dd.congj_ring_num # 2
    #non_congj_ring_num = dd.non_congj_ring_num # 3
    #function_group_dict = dd.function_group_dict # {'ke_am': 1, 'ke': 1, 'ene': 2}
    #aro_ring_num = dd.aro_ring_num  # 34
    #non_aro_ring_num = dd.non_aro_ring_num #435
    
    #print(dd.__dict__)
    pl = plt()
    pl.analyze_eles_type()
    pl.analyze_heavy_atom_number()
    pl.analyze_moles_weight()
    pl.analyze_topological_structure()
    pl.analyze_functional_group()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        