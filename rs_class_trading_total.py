#---- Library
import pandas as pd
import xlwings as xw
import importlib as imp

#---- Re-include
import rs_global
imp.reload(rs_global)
from rs_global import *

#---- class
class class_trading_total :
    def __init__(self) :
        pass
        #self.input_path = None

    def def_main(self, input_path = None, filename = None) :
        path_filename = input_path + filename
        #path = r'input_path + filename'
        #path = open(path_filename, 'r')
        self.def_make_dataframe(path_filename)

    def def_make_dataframe(self, path): # 읽어온 가격지수를 데이터프레임화 하는 함수
        app =xw.App(visible=False)
        wb = xw.Book(path) # xw가 엑셀파일을 read
        sheet = wb.sheets['매매종합'] # sheet 선택
        row_num = sheet.range(1,1).end('down').end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        raw_data = sheet[data_range].options(pd.DataFrame, index = False, header = True).value

        dpt(raw_data)
        app.kill()




