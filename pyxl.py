from multiprocessing import Pool

import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx')

obj = wb.active

sheetNames  = wb.sheetnames
print(sheetNames)
# print()

def readExcel():
    df = pd.read_excel('C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx',sheet_name=sheetNames)

    print(df.keys())
    
readExcel()
# print('\n')
# list(map(readExcel, sheetNames))
   