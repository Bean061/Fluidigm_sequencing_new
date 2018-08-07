from Bio import SeqIO
from Bio import AlignIO

align = AlignIO.read("/Users/zhouwenbin/proj/ipyrad/Hybrid_test/TT4_3/TT4_new2.phy", "phylip") # phylip file should be export by software.
length =len(align)
print length
# check the number of character "-", if it is great than 0,

len = align.get_alignment_length()
sum2 = align[:,len:len+1]

for i in range(len):#inside range is the length of sequence, so is sum2. Should be changed everytime!!

#	if i + 10 < 1992:
    if align[1, i] != align[2, i]:
# == align[3, i] == align[4, i] == align[5, i] == align[6, i] == align[7, i] == align[8, i]
#!= "N" and align[0, i] != "A" and align[0, i] != "T" and align[0, i] != "C" and align[0, i] != "G":   #input the line number of, the first sequence is "0".
        sum2 = sum2 + align[:, i:i+1]
print sum2
SeqIO.write(sum2, "/Users/zhouwenbin/proj/ipyrad/Hybrid_test/TT4_3/TT4_new_hybrid_loci.phy", "phylip")

align[:, i].count("A")