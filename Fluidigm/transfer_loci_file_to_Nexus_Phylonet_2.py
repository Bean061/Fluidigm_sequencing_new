# -*- coding:utf-8 -*-

#####
import xlrd
wb = xlrd.open_workbook('/Users/zhouwenbin/proj/Test_loci/name.xls')
sh = wb.sheet_by_index(0)
print sh.cell_value(0,0)


f1 = open("/Users/zhouwenbin/proj/Test_loci/M50_loci.nex", 'r') # open the the .tre file.
s = len(f1.readlines())
f1.close()  #print how many lines are there in the file, which will be used for the loop.


#f1 = open("/Users/zhouwenbin/proj/Test_loci/M50.loci", 'r')
#sum = ""
#for row in range(sh.nrows):   #查看xls里面第一个数据
    #print row    #print str(sh.cell_value(row, 0))
f1 = open("/Users/zhouwenbin/proj/Test_loci/M50_loci.nex", 'r')
e = 0
c =0
for n in range(s):
        #查看file里面第一行数据
        #print "ss" + str(n)
    text = f1.readline()
        #print text #row_number = i
    if text.find("[") == 0:
        number = text.find(",")
        number2 = text.rfind("]")
        a = text[number + 2:number2]
            #sum = sum + text
        fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci2.txt", 'a')  # you can change your output file name here.
        fw.write(text)
        fw.close()
            #m = n + 1
    #elif text.find("QC_60")
    else:
        blank = text.find(" ")
        b = text[:blank]

        for row in range(sh.nrows):
            for column in range(sh.ncols):
                if b == sh.cell(row, column).value:
                    c = row # CC31  c=0  n =1  CC_32   c=1   n =2  CC_35  n = 3  c = 3  CH_39  n = 4  c = 7  CH_40 n =5 c =8
        if n == 1:
            if c == e:
                fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci2.txt",
                      'a')  # you can change your output file name here.
                fw.write(text)
                fw.close()
                e = c
        else:
            if c - e == 1:
                fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci2.txt",
                          'a')  # you can change your output file name here.
                fw.write(text)
                fw.close()
                e = c
            else:
                d = int(c - e)
                sum = ""
                for m in range(d-1):   ####注意修改10
                    add_line = str(sh.cell_value(c - (m + 1), 0)) + (10 - len(
                        str(sh.cell_value(c - (m + 1), 0)))) * " " + int(a) * "?" + "\n"
                    sum = add_line + sum
                sum = sum + text
                fw = open("/Users/zhouwenbin/proj/Test_loci/M50_loci2.txt", 'a')  # you can change your output file name here.
                fw.write(sum)
                fw.close()
                e = c

f1.close()



####如果缺少最后几个外类群的话，如何添加。