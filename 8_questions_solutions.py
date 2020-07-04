# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:28:21 2020

@author: 585634
"""


import random
def calc_values():
    i=1   
    list1=[]
    while i<=64:
        list1.append(i)
        i=i+1
    return list1

def pop_list(list1,val1):
    for l in list1:
        if(l==val1):
            list1.remove(l)
    return list1

def org_values(list1, Value):
                num1=l
                num2=l
                if(l%8!=0):
                                #Remove value leftwards -Row
                                while (num1)%8!=0:
                                                list1=pop_list(list1,num1)
                                                
                                                num1=num1-1
                
                                #Remove value towards right -Row
                                while (num2)%8!=0:
                                                num2=num2+1
                                                list1=pop_list(list1,num2)
                                                
                else:
                                #Remove value leftwards
                                num1=num1-1
                                while (num1)%8!=0:
                                                list1=pop_list(list1,num1)
                                                
                                                num1=num1-1
                                num2=num2-1    
                                #Remove value towards right-Row
                                while (num2)%8!=0:
                                                num2=num2+1
                                                list1=pop_list(list1,num2)
                                                    
                
                num3=l
                ##Remove value to Bottom"
                while (num3/8>1):
                                num3=num3-8
                                list1=pop_list(list1,num3)
                                
                
                
                #Remove "Value to Top"
                num4=l
                while (num4/8<=8):
                                list1=pop_list(list1,num4)
                                      
                                num4=num4+8   
                
                #REmove "Value to Forward Up -diagonally"
                num5=l
                while (num5/8>1)and(num5%8!=0):
                                num5=num5-7
                                list1=pop_list(list1,num5)
                               
                                
                #print("Value to Forward Down")
                num6=l
                while (num6/8<=8)and(num6%8!=0):
                                num6=num6+9
                                list1=pop_list(list1,num6)
                                
                
                #print("Value to Backward Up" - 
                num7=l    
                while (num7/8>1)and((num7-1)%8!=0):
                                num7=num7-9
                                list1=pop_list(list1,num7)
                                
                
                # remove "Value to Backward Down"-straight
                num8=l    
                while (num8/8<=8)and((num8-1)%8!=0):
                                num8=num8+7
                                list1=pop_list(list1,num8)
                                 
                #print(list1)
                return list1
Empty_list=[]
list2=[]
i=0
while(len(list2)!=8):
    i=i+1
    list1=calc_values()
    list2=[]
    while(len(list1)!=0):
        l=random.choice(list1)
        list2.append(l)
        
        list1=org_values(list1, l)
    if len(list2)==8:
        list2.sort()
       
        print("\n")
i=0
for l in list2:
   list2[i]=(l-1)-(i*8) 
   i=i+1
print(list2) #Display Successful list
