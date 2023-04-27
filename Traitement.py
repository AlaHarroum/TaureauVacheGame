import random

from tkinter import messagebox
from tkinter import *



class TraitementNum:
    def __init__(self, num):
        self.num=num

    def check_num(self,num1):
        return int(num1)


    def check_len(self,num1):
        ch= str(num1)
        if(len(ch)==4):
            return True
        else:
            return False

    def check_occ(self, num1):
        ch=str(num1)
        if(self.check_len(num1) and self.check_num(num1)):
            test=True
            i=0
            while(i<len(ch)-1 and test):
                if(ch[i] not in ch[i+1:]):
                    i+=1
                else:
                    test=False
            return test        
        else:
            messagebox.showinfo('WRONG', 'Enter a valid Integer !')            
        
                

    def countTV(self,num1):
        bull_cow = [0,0]
        ch_rand=str(num1)
        ch_org=str(self.num)
        for i in range(4):
            for j in range(4):
                if(ch_org[i]==ch_rand[j]):
                    if(i==j):
                        bull_cow[0]+=1
                    else:
                        bull_cow[1]+=1
        return bull_cow

    
               


                         




