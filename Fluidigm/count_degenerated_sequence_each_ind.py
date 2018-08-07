from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os

#AC = align[:, i].count("M")
#AG = align[:, i].count("R")
#AT = align[:, i].count("W")
#GT = align[:, i].count("K")
#CG = align[:, i].count("S")
#CT = align[:, i].count("Y")
#sum1 = 0
# phylip, nexus, fasta, fastq
sum1 = "species" + "\t" + "total_sequence" + "\t" + "total_degenerated" + "\t" + "N_number" + "\t" + "M_number" + "\t" + "R_number" + "\t" + "W_number" + "\t" + "K_number" + "\t" + "S_number" + "\t" + "Y_number" + "\n"
file = open("/Users/zhouwenbin/proj/total_sum_degenerated.txt", "a")
file.write(sum1)

for test in SeqIO.parse('/Users/zhouwenbin/Desktop/ML_tree/ML_tree_Castanea/M50.phy','phylip'):
    #print test.description
    a = test.seq.upper()
    count_N = a.count("N")
    count_M = a.count("M")
    count_R = a.count("R")
    count_W = a.count("W")
    count_K = a.count("K")
    count_S = a.count("S")
    count_Y = a.count("Y")
    sum_de = count_M + count_R + count_W + count_K + count_S + count_Y
    length = len(a)
    print length
    print count_N
    #frequency = float(count)/float(length)
    #if frequency < 0.3:
    #    sum1 = sum1 + 1
    sum2 = test.description + "\t" +str(length) + "\t" + str(sum_de) + "\t" + str(count_N) + "\t" + str(count_M) + "\t" + str(count_R) + "\t" + str(count_W) + "\t" + str(count_K) + "\t" + str(count_S) + "\t" + str(count_Y) + "\n"
    print sum2
    file.write(sum2)

file.close()
#print sum1  +str(frequency