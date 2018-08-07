# for fluidigm sequencing.
from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os
wb = xlrd.open_workbook('/Users/xianglab/proj/fluidigm/Per_locus/primer_name.xls')
sh = wb.sheet_by_index(0)

for i in range(48):
	path = "/Users/xianglab/proj/fluidigm/Per_locus/Ind" +str(i+1)
	os.mkdir(path)
	filename = "/Users/xianglab/proj/fluidigm/filter" + str(i+1) + ".fastq"
	for test in SeqIO.parse(filename,'fastq'):
		#print test.description
		for m in range(48):
			if test.description.find(str(sh.cell_value(m,0))) > 0:
				file = "/Users/xianglab/proj/fluidigm/Per_locus/Ind" +str(i+1) + "/Locus" +str(m+1)
				f1 = open(file, 'a')
				SeqIO.write(test, f1, "fastq")
				f1.close()