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
cnt=0
score=0
ans=str(input("GameStart(Y/N): "))
if(ans=='Y'):
    while(1):
        
        userid=str(input("Userid: "))       
       
        A = 0
        B = 0
        number = int(input("請輸入你要猜的數字："))
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
        
        score=10*A+5*B        
        dict1[userid]=score       
        
        print("-------------排行榜-------------") 
        dict= sorted(dict1.items(), key=lambda d:d[1], reverse = True)
        tuple1=tuple(dict)
        for m in range(len(tuple1)):
                print("%2d."%(m+1),"%8s"%dict[m][0],"       ","%2d"%dict[m][1],"分")
else:
    sys.exit()
