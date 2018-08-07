import os
import xlrd
for i in range(51):
    path = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i)
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i) + ".phy"
    output_name = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i) + "/Locus" + str(i)
    output_directory = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus"  + str(i)
    if os.path.isfile(fname) == True:
        #os.mkdir(path)
        cmd = "/Users/zhouwenbin/tools/standard-RAxML-master/raxmlHPC-PTHREADS-SSE3 -f a -x 12345 -p 12345 -# 1000 -m GTRGAMMA -s " + fname +" -n ex -T 4 -w " + output_directory
        print cmd
        os.system(cmd)

for i in range(51):
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i) + ".phy"
    if os.path.isfile(fname) == True:

        wb = xlrd.open_workbook('/Users/zhouwenbin/PycharmProjects/Fluidigm/Nyssa_name2.xls') # open the excel file
        result_tree = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i) + "/RAxML_bipartitions.ex"
        result_modified_tree = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/phy/Locus" + str(i) + "/result" + str(i)
        f1=open(result_tree,'r') # open the the .tre file.
        fw=open(result_modified_tree,'w')  #you can change your output file name here.

        s = len(f1.readlines())
        f1.close()

        f1=open(result_tree,'r')
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
