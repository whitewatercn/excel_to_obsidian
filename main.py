import xlrd


book = xlrd.open_workbook('data/input.xls')
sheet = book.sheet_by_index(0)


numbers=2


for i in range(1,numbers):
	# 逐行获取源数据
	line1 = str('line1：')+ str('[[') + str(sheet.cell_value(rowx=i,colx=0))+ str(']]') + str('\n')
	line2 = str('line2：')+ str('[[') + str(sheet.cell_value(rowx=i,colx=0))+ str(']]') + str('\n')


	ls = [
		line1,
		line2
	]

	# 写入文件

	f = open('output/{}.md'.format(i),'x')
	f.writelines(ls)
	f.close()