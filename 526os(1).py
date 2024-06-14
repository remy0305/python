import os
import time

#print(os.system("notepad.exe"))#開啟記事本
#print(os.system("calc.exe"))#開啟計算機
#print(os.name)#與取得當前使用平台 #window用nt，linux用posix表示  
#print(os.getcwd())#取得當前的工作目錄
#os.rmdir('./text')#刪除資料夾
#os.mkdir('./text')#創建資料夾
list =os.listdir('./text')
print(list)
f=open ( "./text/a.txt",'w',encoding='utf-8')
f.write("abcdef")
f.close()
x=open("./text/a.txt",'r',encoding='utf-8')
print(x.read())