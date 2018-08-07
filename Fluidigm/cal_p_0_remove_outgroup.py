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
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Locus" + str(j) +".phy"
    fname2 = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Phy/Without_outgroup/Locus" + str(j) +".phy"
    print fname
    if os.path.isfile(fname) == True:
#check the line number
        f1=open(fname,'r') # open the the .tre file.
        row_number = len(f1.readlines()) #row_number-1
        f1.close()

        align = AlignIO.read(fname, "phylip") # phylip file should be export by software.
        length = align.get_alignment_length()

# print length
# check the number of character "-", if it is great than 0.
        sum2 = align[:,length:length+1]
        row_initial = align[0,:]
        row_sum = MultipleSeqAlignment([row_initial])
        sum3 = 0

        for j in range(row_number-2):
    # remove the outgroup with same sequence id
    # align[j + 1, :].id != "Ind50" and align[j + 1, :].id != "Ind51" and
            #if align[j+1,:].id != "Ind52" and align[j+1,:].id != "Ind53" and align[j+1,:].id != "Ind54" and align[j+1,:].id != "Ind55" and align[j+1,:].id != "Ind56":
            if align[j + 1, :].id != "Ind50" and align[j + 1, :].id != "Ind51":
                row_sum.append(align[j+1, :])

        SeqIO.write(row_sum, fname2, "phylip")
