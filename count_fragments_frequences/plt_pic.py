#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:33:10 2021

@author: silicon
"""
#import pandas as pd                   
import matplotlib.pyplot as plt       
import numpy as np                    


class plot_bar_pie():
    
    def __init__(self):
        pass

    def plt_bar(self, x,y,title,pic_name):                                                                               
                                                                                                  
        params = {'figure.figsize': '20, 12'}                                                     
        plt.rcParams.update(params)                                                               
                                                                                                  
        fig, ax = plt.subplots()                                                                  
        ax.bar(x, y, width=0.35, align='center', color='blue', alpha=0.8)                                            
        #plt.xlabel(x, size='small',rotation=30)                                                                                          
        plt.title(title, loc='center', fontsize='25',            
              fontweight='bold', color='black')  
        plt.xticks(fontsize='20')
        plt.yticks(fontsize='20')
        plt.xlabel("Number of Paraents' Molecules(lg)",fontsize='20')
        plt.ylabel("Number of fragments",fontsize='20')
        for a,b in zip(x,y):
            plt.text(a,b+0.01,'%.0f'%b, ha='center',va='bottom',fontsize=20)                                              
        plt.savefig(pic_name)                                                                  
        plt.show() 
                                                                               
    def plt_bar_1(self, x,y,title,pic_name):                                                                               
                                                                                                  
        params = {'figure.figsize': '20, 12'}                                                     
        plt.rcParams.update(params)                                                               
                                                                                                  
        fig, ax = plt.subplots()                                                                  
        ax.bar(x, y, width=0.35, align='center', color='blue', alpha=0.8)                                            
        #plt.xlabel(x, size='small',rotation=30)                                                                                          
        plt.title(title, loc='center', fontsize='25',            
              fontweight='bold', color='black')  
        plt.xticks(fontsize='20')
        plt.yticks(fontsize='20')
        plt.xlabel("Number of heavy atoms",fontsize='20')
        plt.ylabel("Number of fragments",fontsize='20')
        for a,b in zip(x,y):
            plt.text(a,b+0.01,'%.0f'%b, ha='center',va='bottom',fontsize=20)                                              
        plt.savefig(pic_name)                                                                  
        plt.show()           
    def plt_h_bar (self, x,y,title,picture_name):

        #y_11 = []
        #for i in range(len(y)):
        #    y_11.append(int(float(y[i])))
        
        params = {'figure.figsize': '20, 50'}                                          
        plt.rcParams.update(params)                                                                                                                       
        fig, ax = plt.subplots()   
        x1 = np.arange(len(x))
        #print(x1,y)                                            
        b1 = plt.barh(x1, y, color='red',height=0.3, label="")                            
                                                                                   
        #设置Y轴纵坐标上的刻度线标签。                                                           
        plt.yticks(range(len(x)),x,size=20)                                                                                                    
        plt.xticks(())     
    
        for rect in b1:                                                             
            w = rect.get_width()                                                   
            ax.text(w, rect.get_y()+rect.get_height()/2, '%d' %                    
                    int(w), ha='left', va='center',fontsize=8) 
                                                                    
        #plt.legend(["chembl","qm"],loc='upper right',fontsize=20)                                                        
        plt.title(title, loc='center', fontsize='25',
                  fontweight='bold', color='black')                                
        plt.savefig(picture_name)                                                         
        plt.show()  
    
    def plt_pie (self,labels,value,explode,title, picture_name):
        plt.figure(figsize=(6,6)) 
        plt.pie(value,explode=explode,labels=labels,
        autopct='%1.1f%%')
        plt.savefig(picture_name)                                                         
        plt.show() 
        
        
        
        
        
        
        
        
        
        
        
        
        