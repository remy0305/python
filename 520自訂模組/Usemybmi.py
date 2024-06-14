import mybmi  # 匯入自訂模組 mybmi
mybmi.name="王曉明" 
# 設定 mybmi 模組中的 name 屬性為 "王曉明"
print("姓名=",mybmi.name) # 輸出 "姓名=" 和 mybmi.name 的值
r = mybmi.bmi(1.75, 75) 
# 計算身高 1.75 公尺、體重 75 公斤的 BMI 值，並將結果賦值給變數 r
print("BMI值=",r) # 輸出 "BMI值=" 和變數 r 的值