#數字三角形
a=int(input())
if a>=100:
    print("請輸入小於100數")
else:
    for i in range (1,a+1):
         for j in range (1,i+1):
           print(f"{i*j:4d}",end="")
         print()      
         

 



 

