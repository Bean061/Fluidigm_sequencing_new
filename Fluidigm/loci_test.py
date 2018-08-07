# -*- coding:utf-8 -*-
import xlrd
wb = xlrd.open_workbook('/Users/zhouwenbin/proj/Test_loci/name.xls')
sh = wb.sheet_by_index(0)
print sh.cell_value(0,0)




f1=open("/Users/zhouwenbin/proj/Test_loci/M50.loci",'r') # open the the .tre file.
s = len(f1.readlines())
f1.close()  #print how many lines are there in the file, which will be used for the loop.
sum = ""
a = 0



#f1 = open("/Users/zhouwenbin/proj/Test_loci/M50.loci", 'r')
#sum = ""
#for row in range(sh.nrows):   #查看xls里面第一个数据
    #print row    #print str(sh.cell_value(row, 0))
#    sum = ""
f1 = open("/Users/zhouwenbin/proj/Test_loci/M50.loci", 'r')
for n in range(s):
        #查看file里面第一行数据
        #print "ss" + str(n)
    text = f1.readline()   #读取每一行数据，包括加一的数据。
        #print text #row_number = i
    a = len(text) - 12
    if text.find(str(sh.cell_value(n,0))) != 0:   #如果cell value = 第一行数据
        add_line = str(sh.cell_value(n, 0)) + (11 - len(str(sh.cell_value(n, 0)))) * " " + a * "?" + "\n"
        sum = sum + add_line + text
        for i in range(s):
            text = f1.readline()
            sum = sum + text
        f1.close()
        fw = open("/Users/zhouwenbin/proj/Test_loci/M50.loci", 'w')  # you can change your output file name here.
        fw.write(sum)
        fw.close()

    else:
        sum = sum + text
        print sum


