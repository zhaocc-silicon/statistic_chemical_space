#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:33:58 2021

@author: silicon
"""

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions
#import pymysql
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
from io import BytesIO

elem_table = {"H": [1, 1.008, [0.3], ],
                  "He": [2, 4.003, [1.16], ],
                  "Li": [3, 6.941, [1.23], ],
                  "Be": [4, 9.012, [0.89], ],
                  "B": [5, 10.811, [0.88]],
                  "C": [6, 12.011, [0.77]],
                  "N": [7, 14.007, [0.70]],
                  "O": [8, 15.999, [0.66]],
                  "F": [9, 18.988, [0.58]],
                  "Ne": [10, 20.170, [0.55]],
                  "Na": [11, 22.990, [1.40]],
                  "Mg": [12, 24.305, [1.36]],
                  "Al": [13, 26.982, [1.25]],
                  "Si": [14, 28.085, [1.17]],
                  "P": [15, 30.974, [1.05]],
                  "S": [16, 32.060, [1.01]],
                  "Cl": [17, 35.453, [0.99]],
                  "Ar": [18, 39.940, [1.55]],
                  "K": [19, 39.089, [2.03]],
                  "Ca": [20, 40.080, [1.74]],
                  "Sc": [21, 44.956, [1.44]],
                  "Ti": [22, 47.900, [1.32]],
                  "V": [23, 50.941, [1.20]],
                  "Cr": [24, 51.996, [1.13]],
                  "Mn": [25, 54.938, [1.17]],
                  "Fe": [26, 55.840, [1.16]],
                  "Co": [27, 58.933, [1.16]],
                  "Ni": [28, 58.690, [1.15]],
                  "Cu": [29, 63.540, [1.17]],
                  "Zn": [30, 65.380, [1.25]],
                  "Ga": [31, 69.720, [1.25]],
                  "Ge": [32, 72.590, [1.22]],
                  "As": [33, 74.922, [1.21]],
                  "Se": [34, 78.900, [1.17]],
                  "Br": [35, 79.904, [1.14]],
                  "Kr": [36, 83.800, [1.89]],
                  "Rb": [37, 85.467, [2.25]],
                  "Sr": [38, 87.620, [1.92]],
                  "Y": [39, 88.906, [1.62]],
                  "Zr": [40, 91.220, [1.45]],
                  "Nb": [41, 92.906, [1.34]],
                  "Mo": [42, 95.940, [1.29]],
                  "Tc": [43, 99.000, [1.23]],
                  "Ru": [44, 101.070, [1.24]],
                  "Rh": [45, 102.906, [1.25]],
                  "Pd": [46, 106.420, [1.28]],
                  "Ag": [47, 107.868, [1.34]],
                  "Cd": [48, 112.410, [1.41]],
                  "In": [49, 114.820, [1.50]],
                  "Sn": [50, 118.600, [1.40]],
                  "Sb": [51, 121.700, [1.41]],
                  "Te": [52, 127.600, [1.37]],
                  "I": [53, 126.905, [1.33]],
                  "Xe": [54, 131.300, [2.09]],
                  "Cs": [55, 132.905, [2.35]],
                  "Ba": [56, 137.330, [1.98]],
                  "La": [57, 138.905, [1.69]],
                  "Ce": [58, 140.120, [1.65]],
                  "Pr": [59, 140.910, [1.65]],
                  "Nd": [60, 144.200, [1.64]],
                  "Pm": [61, 147.000, [1.64]],
                  "Sm": [62, 150.400, [1.66]],
                  "Eu": [63, 151.960, [1.85]],
                  "Gd": [64, 157.250, [1.61]],
                  "Tb": [65, 158.930, [1.59]],
                  "Dy": [66, 162.500, [1.59]],
                  "Ho": [67, 164.930, [1.58]],
                  "Er": [68, 167.200, [1.57]],
                  "Tm": [69, 168.934, [1.56]],
                  "Yb": [70, 173.000, [1.70]],
                  "Lu": [71, 174.960, [1.56]],
                  "Hf": [72, 178.400, [1.44]],
                  "Ta": [73, 180.947, [1.34]],
                  "W": [74, 183.800, [1.30]],
                  "Re": [75, 186.207, [1.28]],
                  "Os": [76, 190.200, [1.26]],
                  "Ir": [77, 192.200, [1.26]],
                  "Pt": [78, 195.080, [1.29]],
                  "Au": [79, 196.967, [1.34]],
                  "Hg": [80, 200.500, [1.44]],
                  "Tl": [81, 204.300, [1.55]],
                  "Pb": [82, 207.200, [1.54]],
                  "Bi": [83, 208.980, [1.52]],
                  "Po": [84, 209.000, [1.53]],
                  "At": [85, 210.000, [1.52]],
                  "Rn": [86, 222.000, [1.53]],
                  "Fr": [87, 223.000, [2.45]],
                  "Ra": [88, 226.030, [2.02]],
                  "Ac": [89, 227.000, [1.70]],
                  "Th": [90, 232.030, [1.63]],
                  "Pa": [91, 231.030, [1.46]],
                  "U": [92, 238.020, [1.40]],
                  "EP": [0, 0.0, [0.0]],
                  "Bq": [0, 0.0, [0.0]],
                  "XX": [0, 0.0, [0.0]],
                  }


class get_mol_attr():
    
    def __init__(self,smiles):
        self.smiles = smiles
        self.isring = False
        self.num_ring = 0
        #self.is_congj_ring = False
        self.congj_ring_num = 0
        self.non_congj_ring_num = 0
        
        self.ring_size = []
        self.mass = 0
        self.heavy_atoms = []
        self.all_atoms = []
        #self.is_fuse_ring = False
        self.fuse_ring_num = 0
        self.non_fuse_ring_num = 0
        
        self.get_eles()
        self.get_ring()
        self.cal_mass()
        self.juduge_fuse_ring()
    def get_eles(self):
             
        mol = Chem.MolFromSmiles(self.smiles)
        atoms = mol.GetAtoms()
        for atom in atoms:
            self.heavy_atoms.append(atom.GetSymbol())
            
        mol2 = Chem.AddHs(mol)
        atoms = mol2.GetAtoms()
        #i = 0
        for atom in atoms:
            #print(i, atom.GetSymbol(), end = ",")
            #i = i+1
            self.all_atoms.append(atom.GetSymbol())
    
    def show_str(self):
        opts =  DrawingOptions() 

        mol = Chem.MolFromSmiles(self.smiles)
       
        #mol = Chem.AddHs(mol)
        m = self.mol_with_atom_index(mol)

        opts.atomLabelFontSize=400
        opts.atomLabelMinFontSize = 300
        opts.includeAtomNumbers=True
        opts.dblBondLengthFrac=0.8
        opts.includeAtomNumbers=True
        opts.dotsPerAngstrom = 10000
        #img = Draw.MolToImage(mol, options=opts)
        img = Draw.MolToImage(m, options=opts, size=(500,500))
        img.save("test_2.png")
        img.show()
        
    def show_str_1(self,central_atoms):
        mol = Chem.MolFromSmiles(self.smiles)
        mol_highlightBonds = mol.GetBondBetweenAtoms(central_atoms[0],central_atoms[1]).GetIdx()   
        d = rdMolDraw2D.MolDraw2DCairo(500, 500)
        rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=[], highlightBonds=[mol_highlightBonds])

        d.FinishDrawing()
        png = d.GetDrawingText()
        bio = BytesIO(png)
        img = Image.open(bio)   
        img.save("my_mol.png")
        
    def mol_with_atom_index(self, mol ):
        atoms = mol.GetNumAtoms()
        for idx in range( atoms ):
            mol.GetAtomWithIdx( idx ).SetProp( 'molAtomMapNumber', str( mol.GetAtomWithIdx( idx ).GetIdx() ) )
        return mol
        
    def get_ring(self):
        mol = Chem.MolFromSmiles(self.smiles)
        ssr = Chem.GetSymmSSSR(mol)
        self.num_ring = len(ssr)
        if self.num_ring>0:
            self.isring = True
            
            for ring in ssr:
                ring_atom_id = list(ring)
                ring_size = len(ring_atom_id)
                self.ring_size.append(ring_size)
                is_congj_ring = False
                for a_id in ring_atom_id:
                    atom = mol.GetAtomWithIdx(a_id) # get-atom by id
                    bonds = atom.GetBonds()   #get bonds object
                    flag = False
                    for bond in bonds:
                        if bond.GetIsConjugated():
                            is_congj_ring = True
                            #self.congj_ring_num +=1
                            flag = True
                            break
                    if flag:
                        break
                if is_congj_ring:
                    self.congj_ring_num +=1
                else:
                    self.non_congj_ring_num += 1
                            
                            
    def cal_mass(self):
        for ele in self.all_atoms:
            self.mass += float(elem_table[ele][1])
            
    def juduge_fuse_ring(self):
        #寻找稠环算法，两个环有相同的原子，并且这两个原子是相邻的
        mol = Chem.MolFromSmiles(self.smiles)
        #print(self.smiles)
        ssr = Chem.GetSymmSSSR(mol)
        ring_atoms = []
        fuse_ring_id = []
        if len(ssr) >0:
            for ring in ssr:
                ring_atoms.append(list(ring))
        
            for i in range(len(ring_atoms)-1):
                for j in range(i+1,(len(ring_atoms))):
                    #print(ring_atoms)
                    a = set(ring_atoms[i])  #ring a
                    b = set(ring_atoms[j])  # ring b
                    #print("rings",a,b)
                    inter_atom_id = a & b
                    #print("iner",inter_atom_id)
                    if len(inter_atom_id) > 1:
                        for idx in inter_atom_id:
                            #print("idx",idx)
                            atom = mol.GetAtomWithIdx(idx)
                            neighbor_atoms = atom.GetNeighbors()
                            #print(neighbor_atoms)
                            nei_atomid_list = []
                            for nei_atom in neighbor_atoms:
                                nei_id = nei_atom.GetIdx()
                                #print("nei_id",nei_id,nei_atom.GetAtomicNum())
                                nei_atomid_list.append(nei_id)
                            #print(set(nei_atomid_list ) , inter_atom_id)
                            if len(set(nei_atomid_list ) & inter_atom_id) >0:
                                #self.is_fuse_ring = True
                                fuse_ring_id.append(i)
                                fuse_ring_id.append(j)
                                break
            fuse_ring_id = list(set(fuse_ring_id))
            self.fuse_ring_num = len(fuse_ring_id)   
            self.non_fuse_ring_num =  len(ssr)- len(fuse_ring_id)              
                
                                           
if __name__ == "__main__":
    #gma = get_mol_attr('OC1C2C1CC2')
    gma = get_mol_attr('c1cnc(C2CCCN2c2cnccn2)cn1')
    gma.show_str()
    #gma.show_str_1([1,2])
    #gma.get_eles()
    #gma.get_ring()
    #gma.cal_mass()
    #print(gma.__dict__)  
    #print(gma.mass)

    