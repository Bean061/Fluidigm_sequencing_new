#This script is used for changing the labels in the tree.
# #Wenbin Zhou
#wzhou10@ncsu.edu
#You need to prepare two files. One aimed file and one excel (xls) file. The xls file should be with two columns: 1st is original name, 2nd is the replaced name.

import xlrd
wb = xlrd.open_workbook('/Users/zhouwenbin/PycharmProjects/Fluidigm/Nyssa_name.xls') # open the excel file
f1=open("/Users/zhouwenbin/proj/Con_tre",'r') # open the the .tre file.
fw=open("/Users/zhouwenbin/proj/result2",'w')  #you can change your output file name here.

s = len(f1.readlines())
f1.close()

f1=open("/Users/zhouwenbin/proj/Con_tre",'r')
sum = ""
for i in range(s):
    text = f1.readline()
    print text
    sh = wb.sheet_by_index(0)
    for row in range(sh.nrows):
        text = text.replace(str(sh.cell_value(row,0)),str(sh.cell_value(row,1)))
    sum = text
#dic[str(sh.cell_value(row,0))]=str(sh.cell_value(row,1))
    fw.write (sum)


fw.close()
f1.close()
