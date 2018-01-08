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
    print("成績: %dA%dB      得分: %2d分 \n\n" % (A, B, op_score(A,B)))
    return op_score(A,B)

def op_score(X,Y):
    return 10*X+5*Y

def show_list(SortedList):
    
    print("---------排行榜---------") 
    for m in range(len(SortedList)):
        print("%2d.%8s         %2d分"%(m+1,SortedList[m][0],SortedList[m][1]))
    #write_list(SortedList) # write rank into "file.txt"
    return

def write_list(List):    
    name = open('file.txt','w',encoding = 'UTF-8')
    score = open('file1.txt','w',encoding = 'UTF-8')
    for m in range(len(List)):
        name.write(List[m][0]+"\n")
        score.write(str(List[m][1])+"\n")
    name.close()
    score.close()
    return

def read_list():
    name = open('file.txt','r',encoding = 'UTF-8')
    score = open('file1.txt','r',encoding = 'UTF-8')
    n = name.readlines()
    s = score.readlines()     
    for m in range(len(n)):
        tmp_n = n[m]
        tmp_n = tmp_n.strip() # delete '\n'
        tmp_s = s[m]
        tmp_s = int(tmp_s)    # turn str(score) -> int(score)
        dict1[tmp_n] = tmp_s
    name.close()
    score.close()
    return    

# main function
ans=str(input("GameStart(Y/N): "))
if(ans=='Y'):
    read_list()
    ranklist = sorted(dict1.items(), key=lambda d:d[1], reverse = True) # generate rank list 
    show_list(ranklist) # show rank list
    while(1):
        userid=str(input("Userid: "))        
        inputNumber = int(input("請輸入你要猜的數字："))    
        score=show_1A2B(inputNumber) #show 1A2B and operate score        
        dict1[userid]=score  # store user and  to dictionary
        ranklist = sorted(dict1.items(), key=lambda d:d[1], reverse = True) # generate rank list             
        write_list(ranklist) # write rank into "file.txt"
        show_list(ranklist)  #show rank list
else:
    sys.exit()
