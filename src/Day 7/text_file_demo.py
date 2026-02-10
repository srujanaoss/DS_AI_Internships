file=open("sample.txt","w")
file.write("Hello, this file handling example")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()


with open("sample.txt","r")as file:
     content=file.read()
     print(content)


#csv file 
import csv
with open("Day 6\data.csv","r")as file:
     read=csv.reader(file)
     for row in read:
          print(row)

# Reading Excel file with openpyxl
import pandas as pd
data=pd.read_csv("Day 6\data.csv")
print(data)

import openpyxl
workbook = openpyxl.load_workbook("Day 6/student.xlsx")
sheet = workbook.active
for row in sheet.iter_rows(values_only=True):
    print(row)
