# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import random

Answer=random.sample(range(10),4)
print(Answer)
dict1={}
ans=0
score=0

def show_1A2B(number):
    A = 0
    B = 0
    four=number%10
    three=((number-four)/10)%10        
    two=((((number-four)/10)-three)/10)%10
    one=((((((number-four)/10)-three)/10)-two)/10)%10
    list2 = []
    list2.extend([one,two,three,four])
    for k in range(4):
        if (Answer[k]==list2[k]):
            A += 1                
    for i in range(4):
        for j in range(4):
            if (Answer[i]==list2[j]):          
                B = B+1                   
    B = B-A
    print("%dA%dB" % (A, B))
    return op_score(A,B)

def op_score(X,Y):
    return 10*X+5*Y

def show_dict1():
    
    print("-------------排行榜-------------") 
    dict = sorted(dict1.items(), key=lambda d:d[1], reverse = True)
    tuple1=tuple(dict)
    for m in range(len(tuple1)):
        print("%2d.%8s       %2d分"%(m+1,dict[m][0],dict[m][1]))
    return

# main function
ans=str(input("GameStart(Y/N): "))
if(ans=='Y'):
    while(1):        
        userid=str(input("Userid: "))        
        inputNumber = int(input("請輸入你要猜的數字："))
        score=show_1A2B(inputNumber) #show 1A2B and operate score        
        dict1[userid]=score # store user and score
        show_dict1() # show score list
else:
    sys.exit()
