#!/use/bin/env python
#coding:utf-8

#Author:WuYa

import  xlrd

from utils.public import *



class OperationExcel:
	def getExcel(self):
		db=xlrd.open_workbook(data_dir('data','data.xlsx'))
		sheet=db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)

opera = OperationExcel()
print(opera.get_rows())