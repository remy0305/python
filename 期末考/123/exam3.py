from docxtpl import DocxTemplate
import requests
import json

r = requests.get('https://data.moa.gov.tw/Service/OpenData/FromM/AquaticTransData.aspx')
text = json.loads(r.text)
FishName = []

for row in text:
    if row['魚貨名稱'] not in FishName:
        FishName.append(row['魚貨名稱'])

tpl = DocxTemplate("ExamTemplate.docx")

context = {
            "schoolyear" : "112",
            "semester" : "二",
            "subject" : "電腦軟體應用",
            "class" : "五資一甲",
            "studentID" : "51215105",
            "name" : "陳慶恩"
          }
studentID = input("請輸入您的學號:")
studentName =  input("請輸入您的姓名:")
fish = FishName[int(studentID[-2:])]

context["studentID"] = studentID
context["name"] = studentName
context["fish"] = fish


tpl.render(context)
tpl.save("ExaminationPapers.docx")


