from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os


align = AlignIO.read("/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Locus2.phy", "phylip") # phylip file should be export by software.
length = align.get_alignment_length()

# print length
# check the number of character "-", if it is great than 0.
sum2 = align[:,length:length+1]
row_initial = align[0,:]
row_sum = MultipleSeqAlignment([row_initial])

print length

sum4 = 0
for i in range(length):#inside range is the length of sequence, so is sum2. Should be changed everytime!!
    sum3 = 0
#	if i + 10 < 1992:
    A = align[:, i].count("a")
    T = align[:, i].count("t")
    C = align[:, i].count("c")
    G = align[:, i].count("g")
    AC = align[:, i].count("m")
    AG = align[:, i].count("r")
    AT = align[:, i].count("w")
    CG = align[:, i].count("s")
    CT = align[:, i].count("y")
    GT = align[:, i].count("k")
    if A > 0:
        sum3 = sum3 + 1
    if T > 0:
        sum3 = sum3 + 1
    if C > 0:
        sum3 = sum3 + 1
    if G > 0:
        sum3 = sum3 + 1
    if AC > 0:
        sum3 = sum3 + 1
    if AG > 0:
        sum3 = sum3 + 1
    if AT > 0:
        sum3 = sum3 + 1
    if CA > 0:
        sum3 = sum3 + 1
    if CG > 0:
        sum3 = sum3 + 1
    if CT > 0:
        sum3 = sum3 + 1
    print ("Site" + str(i+1) + "\t" + str(sum3))
    if sum3 > 1:
        sum4 = sum4 + 1

file_content = "Total_length" + "\t" + str(length) + "\t" + "Total_number" + "\t" + str(sum4) + "\n"

file = open("/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/f1.txt","a")
file.write(file_content)
file.close()