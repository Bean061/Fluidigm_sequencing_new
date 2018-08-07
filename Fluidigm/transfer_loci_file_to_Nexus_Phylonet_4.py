# -*- coding:utf-8 -*-
import xlrd
import linecache #导出文件的哪一行

wb = xlrd.open_workbook('/Users/zhouwenbin/proj/Test_loci/name.xls')
sh = wb.sheet_by_index(0)
print sh.cell_value(0,0)


f1 = open("/Users/zhouwenbin/proj/Test_loci/M50_loci3.txt", 'r')
s = len(f1.readlines())
f1.close()

lines = []
f1 = open('/Users/zhouwenbin/proj/Test_loci/M50_loci3.txt','r')
for line in f1:
    lines.append(line)
print lines
f1.close()



f1 = open('/Users/zhouwenbin/proj/Test_loci/M50_loci3.txt','r')
line_num = 0
search_phrase = "["
c = 0
for line in f1.readlines():
    line_num += 1

    if line.find("[") == 0:   ###一但找到"["，就可以进入此循环。

        if line_num ==1:
            fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci4.txt",
                      'a')  # you can change your output file name here.
            fw.write(line)
            fw.close()

        else:
            blank = lines[line_num - 2].find(" ")###看前一行的数据
            b = lines[line_num - 2][:blank]
            #number = line.find(",")
            #number2 = line.rfind("]")
            a = len(lines[line_num - 2]) - 11 ####改变数值12-1
            for row in range(sh.nrows):    ###查看对应的xls里面的行数
                for column in range(sh.ncols):
                    if b == sh.cell(row, column).value:
                        c = row
            print c
            #print sh.nrows
            if c < 25:   #行数-1
                d = int(25-c)   #zongshu
                sum = ""
                for m in range(d):    ####改变数值11-1
                    add_line = str(sh.cell_value(c + m + 1, 0)) + (10 - len(str(sh.cell_value(c + m + 1, 0)))) * " " + int(a) * "?" + "\n"
                    sum = sum + add_line
                sum = sum + line
                fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci4.txt", 'a')  # you can change your output file name here.
                fw.write(sum)
                fw.close()

            else:
                fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci4.txt",
                          'a')  # you can change your output file name here.
                fw.write(line)
                fw.close()
    else:
        fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci4.txt",
                  'a')  # you can change your output file name here.
        fw.write(line)
        fw.close()
f1.close()
