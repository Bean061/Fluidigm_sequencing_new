from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os
import os.path
for j in range(56):
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Without_outgroup/Locus" + str(j) +".phy"
    print fname
    if os.path.isfile(fname) == True:
        align = AlignIO.read(fname, "phylip") # phylip file should be export by software.
        length = align.get_alignment_length()
        print length
# print length
# check the number of character "-", if it is great than 0.
        sum2 = align[:,length:length+1]
        row_initial = align[0,:]
        row_sum = MultipleSeqAlignment([row_initial])
        sum4 = 0
        for i in range(length):#inside range is the length of sequence, so is sum2. Should be changed everytime!!
            sum3 = 0
#	if i + 10 < 1992:
            A = align[:, i].count("A")
            T = align[:, i].count("T")
            C = align[:, i].count("C")
            G = align[:, i].count("G")
            AC = align[:, i].count("M")
            AG = align[:, i].count("R")
            AT = align[:, i].count("W")
            CG = align[:, i].count("S")
            CT = align[:, i].count("Y")
            GT = align[:, i].count("K")
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
            #print ("Site" + str(i+1) + "\t" + str(sum3))
            if sum3 > 1:
                sum4 = sum4 + 1

        file_content = "Length_of_Matrix" +str(j) + "\t" + str(length) + "\t" + "Total_number_of_locus" + str(j) + "\t" + str(sum4) + "\n"

        file = open("/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Without_outgroup/total_sum_poly_withououtgroup.txt","a")
        file.write(file_content)
        file.close()