# -*- coding:utf-8 -*-
import xlrd
import linecache #导出文件的哪一行
###Select which seq should be taken.

wb = xlrd.open_workbook('/Users/zhouwenbin/proj/Test_loci/Torreya_M50/name2.xls')
sh = wb.sheet_by_index(0)
print sh.cell_value(0,0)


f1 = open("/Users/zhouwenbin/proj/Test_loci/Torreya_M50/M50_loci5.txt", 'r')
s = len(f1.readlines())
f1.close()

lines = []
f1 = open('/Users/zhouwenbin/proj/Test_loci/Torreya_M50/M50_loci5.txt','r')
for line in f1:
    lines.append(line)
print lines
f1.close()




line_num = 0
sum = 0
f1 = open('/Users/zhouwenbin/proj/Test_loci/Torreya_M50/M50_loci5.txt','r')
for n in range(s):
    line = f1.readline() ####大循环
    for row in range(sh.nrows):
        if line.find(str(sh.cell(row, 0).value)) != 0:
            sum = sum +1

    if sum == 16:    ####改变
        fw = open("/Users/zhouwenbin/proj/Test_loci/Torreya_M50/M50_loci6.txt", 'a')  # you can change your output file name here.
        fw.write(line)
        fw.close()
    sum = 0
f1.close()
