import requests
import pandas as pd

data = requests.get("https://data.moa.gov.tw/Service/OpenData/FromM/AquaticTransData.aspx?IsTransData=1&UnitId=039").json()
_data = pd.DataFrame(data)

filtered_data = _data[_data['魚貨名稱'].isin([ '烏仔魚'])]
#print(filtered_data)
#filtered_data = filtered_data[~filtered_data['市場名稱'].str.contains('台北|台中')]
#filtered_data = filtered_data.drop(columns=['上價', '中價', '下價'])
filtered_data.to_excel("51215105-2.xlsx", index=False)