import numpy as np
import pandas as pd

def getExcel(filePath):
    df = pd.read_excel(filePath)
    return df

def getExcelWriter(filePath):
    excelWriter=pd.ExcelWriter(filePath,engine="openpyxl")
    return excelWriter

print(getExcel(r"F:\日常工作报告\190505 -周文鑫-工作周报表.xlsx"))