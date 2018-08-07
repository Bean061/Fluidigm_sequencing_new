from Bio import SeqIO
from Bio import AlignIO
import xlrd
import os
align = AlignIO.read("/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Concatenated.phy", "phylip") # phylip file should be export by software.
#len(align)
length = align.get_alignment_length()

wb = xlrd.open_workbook('/Users/zhouwenbin/proj/Fluidigm_matrix/table2.xls') # open the excel file
sh = wb.sheet_by_index(0)
b = 0
for row in range(sh.nrows):
    sum2 = align[:, length:length + 1]
    a = int(sh.cell_value(row,1))
    sum2 = sum2 + align[:, b:(b+a)]
    b = b + a
    filename1 = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Starbeast/" + str(sh.cell_value(row, 0)) + ".phy"
    # check the number of character "-", if it is great than 0,
    SeqIO.write(sum2, filename1, "phylip")

