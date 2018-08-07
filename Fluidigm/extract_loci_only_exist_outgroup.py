from Bio import SeqIO
from Bio import AlignIO

align = AlignIO.read("/Users/zhouwenbin/Desktop/test_loci/M30_new.phy", "phylip") # phylip file should be export by software.
align2 = AlignIO.read("/Users/zhouwenbin/Desktop/test_loci/M40_new.phy", "phylip")
length =len(align)
length2 =len(align)
print length
print length2

# check the number of character "-", if it is great than 0,

len = align.get_alignment_length()
sum2 = align[:,len:len+1]
len2 = align.get_alignment_length()

for i in range(len):#inside range is the length of sequence, so is sum2. Should be changed everytime!!
#	if i + 10 < 1992:
    sum2 = sum2 + align[:, i:i+1]
for j in range(len2):
    sum2 = sum2 + align2[:, j:j + 1]

print sum2
SeqIO.write(sum2, "/Users/zhouwenbin/Desktop/test_loci/M40_total.phy", "phylip")
