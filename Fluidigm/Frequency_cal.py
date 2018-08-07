from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os

sum1 = 0
# phylip, nexus, fasta, fastq
for test in SeqIO.parse('/Users/zhouwenbin/proj/Du/M50.phy','phylip'):
	#print test.description
	a = test.seq.upper()
	count = a.count("N")
	length = len(a)
	frequency = float(count)/float(length)
	if frequency < 0.3:
		sum1 = sum1 + 1
	print (test.description + "\t" +str(length) + "\t" +str(frequency))
print sum1