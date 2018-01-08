# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:13:32 2017

@author: Rightleft
"""

def menu(user1,user2):
    print()
    print("1. 註冊帳號")
    print("2. 登入帳號")    

def menu2(user1,user2):
    print()
    if user1 in data:
        print("使用者: {} 登入中  上次登入時間: {}".format(user1,Time[user1]))
    if user2 in data:
        print("使用者: {} 登入中  上次登入時間: {}".format(user2,Time[user2]))       
    print("1. 回選單")
    print("2. 修改密碼")
    
    print("0. 登出")

def ReadData():
    with open('password.txt','r', encoding = 'UTF-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else: return dict()
        
def ReadTime():
    with open('time.txt','r', encoding = 'UTF-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            time = ast.literal_eval(filedata)
            return time
        else: return dict()
    
def regist_account():
    while True:
        name = input("請輸入帳號: ")
        if name =="": break
        if name in data:
            print("{}帳號已存在!!".format(name))
            continue
        while True:
            password=input("請輸入密碼: ")            
            if regist_judge(password): # 判斷密碼字元
                password=encrypt(password) # 加密
                data[name] = password #存檔
                with open('password.txt','w',encoding='UTF-8-sig') as f:
                    f.write(str(data))
                    print()
                    print("===={}註冊成功====".format(name))
                    break                    
            else:                
                continue        
        break
    
def login(use1):  #登入
    error_cnt=2  
    success=True
    name = input("請輸入帳號: ")            
    while success:
        password=input("請輸入密碼: ")     # 讀密碼      
        if login_judge(name,password):         # 登入成功
            Time[name]=time.strftime("%Y/%m/%d %I:%M:%S")   # 紀錄最後登入時間
            writeTime()
            success=False
            if name==user1:                
                print()
                print("=====重複登入!!!  此帳號登入中=====")
                break
            print()
            print("===={}登入成功====".format(name))            
            if user1==0:
                user[0]=name
                break
            user[1]=name
            break
        else:
            if error_cnt==0:
                print("=====密碼錯誤過多! 已強制登出!=====")
                break
            error_cnt -= 1
            print("==密碼錯誤==")
            continue 
        break                                
        
def drop(s):
    s1 = str(s)
    s1 = s1.strip('b')
    s2 = s1.replace("'","")
    return s2

def encrypt(s):
    msg_text = s.rjust(32)
    secret_key = '1234567890123456' # create new & store somewhere safe
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return drop(encoded.strip())

def decrypt(s):
    msg_text = s.rjust(32)
    secret_key = '1234567890123456' # create new & store somewhere safe
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    decoded = cipher.decrypt(base64.b64decode(msg_text))
    return drop(decoded.strip())
        
def regist_judge(s):
    if not s.islower():        
        if not s.isupper():
            if not s.isalpha():
                if not s.isnumeric():
                    if len(s)>=8:
                        return True
                    else: 
                        print("密碼長度過短!!(至少8位元)")
                        return False
                else:
                    print("密碼須包含大小寫字母")
                    return False
            else:
                print("密碼須包含數字")
                return False
        else:
            print("密碼須包含小寫字母")
            return False
    else:
        print("密碼須包含大寫字母")
        return False
    
def login_judge(Name,psw):    
    decre_password=decrypt(data[Name])# 解密此帳號密碼
    if psw==decre_password: # 密碼正確
        return True
    else:   #密碼錯誤     
        return False

def update_psw(name):              
    while True:        
        password=input("請輸入新密碼: ")     # 讀密碼      
        if regist_judge(password):         # 設定成功  
            password=encrypt(password) # 加密
            data[name] = password #存檔
            with open('password.txt','w',encoding='UTF-8-sig') as f:
                f.write(str(data))
                print()
                print("====密碼設定完成====".format(name))
                break
        else: continue    

def writeTime():
    with open('time.txt','w',encoding='UTF-8-sig') as f:
        f.write(str(Time))

from Crypto.Cipher import AES
import base64, ast, time
data = dict()
Time = dict()
user=[0,0]
user1=0
user2=0
data = ReadData()
Time = ReadTime() #上次登入時間

while True:
    menu(user1,user2)
    choice = int(input(">> "))
    if choice==1:
        regist_account()          # 註冊帳號
    elif choice==2:               # 登入帳號  
        login(user1)        
        if user1==0:              # 第一次登入              
            user1=user[0]
        else:            
            user2=user[1]
        while True:            
            menu2(user1,user2)
            choice = int(input(">> "))
            if choice==1:
                break
            elif choice==2:
                name = input("請輸入要修改的帳號: ")
                update_psw(name)
            else:                 # 登出
                name = input("請輸入要登出的帳號: ")
                if user1==name:
                    user1=0        
                if user2==name:
                    user2=0 
                print("====={}已登出=====".format(name))
    else:
        break