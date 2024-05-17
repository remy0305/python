#找最大公因數和最小公倍數
num1=int(input())
num2=int(input())
b=0

if num1<num2:
    tamp=num1
    num1=num2
    num2=tamp

for a in range (1,num1-1):#最大公因數
    
    if num1%a==0:
        b=a
        print(b)
    if num2%a==0:
        c=a
        print(b)
    if b==c:
        d=b

print("最大公因數是",d)    

e=num1/d
f=num2/d 
answer=e*f*d
print("最小公倍數",answer)