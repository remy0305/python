#去爬google網頁資料
import requests
url ="https://www.google.com"
response= requests.get(url)
if response.status_code==200:
    print(response.text)
    print("編碼:",response.encoding)
else:
    print("error")

