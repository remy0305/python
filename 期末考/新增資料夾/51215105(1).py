import requests
from PIL import Image
import os


url = ["https://imgcdn.cna.com.tw/www/WebPhotos/1024/20220613/999x999_345956001759.jpg","https://i0.wp.com/animal-friendly.co/wp-content/uploads/2022/01/%E5%AD%9F%E5%8A%A0%E6%8B%89%E8%99%8E%EF%BC%88medium%EF%BC%89.jpeg?resize=696%2C435&ssl=1","https://c2.staticflickr.com/8/7376/27466438332_28ea5e5e7a_b.jpg"]
path = "p"
for i, pic in enumerate(url):
    response = requests.get(pic)
    if response.status_code == 200:
        with open(path+str(i+1)+".png", 'wb') as fp:
            for chunk in response:
                fp.write(chunk)
        print("LOGO", i+1,"圖檔已經下載")
        im = Image.open(path+str(i+1)+".png")
        im.show()
    else:
        print("錯誤! HTTP請求失敗...")


p1=Image.open("p1.png")

p2=Image.open("p2.png")

p3=Image.open("p3.png")

p4=Image.open("51215105.png")

x=int(p1.width -p4.width)

y=int(p1.height - p4.height)

p1.paste(p4,(x,y))
p1.save("py1.png")
p1.show()

x=int(p2.width -p4.width)

y=int(p2.height - p4.height)

p2.paste(p4,(x,y))
p2.save("py2.png")
p2.show()

x=int(p3.width -p4.width)

y=int(p3.height - p4.height)

p3.paste(p4,(x,y))
p3.save("py3.png")
p3.show()