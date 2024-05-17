#學校作業
#1. 請簡單說明什麼是變數？何謂運算式與運算子？
#變數就是可以改變的數 運算式是像a+b 運算子是像+
#2. 請指出下列哪一個並不是合法Python識別字（請圈起來？

#Joe、H12_22、_A24、(1234)、test、(1abc)

#3. 請分別一一寫出Python程式敘述來完成下列工作，如下所示：

#Ÿ  建立整數型態的變數num和var，字串型態的變數a，同時指定a的初值'Tom'；var的初值123。
a = "tom"
var = 123
#Ÿ  讓使用者自行輸入變數num的值。
num = input("請輸入整數值==>")
#Ÿ  在螢幕顯示變數a、var和num的值。
print(f"a:{a}""\n")
print(f"var:{var}""\n")
print(f"num:{num}""\n")
#4. 請寫出下列Python運算式的值，如下所示：
NUM1 =1 * 2 + 4
print(f"NUM1:{NUM1}""\n")
NUM2=7 / 5
print(f"NUM2:{NUM2}""\n")
NUM3=10 % 3 * 2 * ( 2 + 5 )
print(f"NUM3:{NUM3}""\n")
NUM4= 1 + 2 ** 3
print(f"NUM4:{NUM4}""\n")
NUM5=(1 + 2) * 3
print(f"NUM5:{NUM5}""\n")
NUM6=16 + 7 * 6 + 9
print(f"NUM6:{NUM6}""\n")
NUM7=(13 - 6 ) / 7 + 8
print(f"NUM6:{NUM7}""\n")
NUM8=12 - 4 % 6 / 4
print(f"NUM8:{NUM8}""\n")

#5. 請寫出下列Python程式碼片段的執行結果，如下所示：
i = 1
i *= 5
i += 2
print(f"i ={i}""\n")
#6. 請寫出下列Python程式碼片段的執行結果，如下所示：
x = y = 7
print(f"x ={x}""\n""y ={y}""\n")
a, b = x, 10
print(f"a ={a}""\n""b={b}""\n")

#7. 圓周長公式是2*PI*r，PI是圓周率3.1415，r是半徑，請建立Python程式定義圓周率變數後，輸入半徑來計算和顯示圓周長。
PI=3.1415
R=float(input("請輸入半徑值=="))
圓周長=2*R*PI
print(f"圓周長={圓周長}""\n")

#8. 計算體脂肪BMI值的公式是W/(H*H)，H是身高（公尺），W是體重（公斤），請建立Python程式輸入身高和體重後，計算和顯示BMI值。

H=float(input("請輸入身高值(公尺)==>"))
W=float(input("請輸入體重值==>"))
BMI=W/(H*H)
print(f"BMI={BMI}""\n")