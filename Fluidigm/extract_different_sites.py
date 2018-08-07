from Bio import SeqIO
from Bio import AlignIO

align = AlignIO.read("/Users/zhouwenbin/proj/50N_82.phy", "phylip") # phylip file should be export by software.
length =len(align)
print length
# check the number of character "-", if it is great than 0,
sum2 = align[:,108554:108555]


for i in range(108554):#inside range is the length of sequence, so is sum2. Should be changed everytime!!

#	if i + 10 < 1992:
    if align[:, i].count("N") == 0:
        sum2 = sum2 + align[:, i:i+1]

SeqIO.write(sum2, "/Users/zhouwenbin/proj/50N_82.fasta", "fasta")



#for i in range(48751):#inside range is the length of sequence, so is sum2. Should be changed everytime!!


#    if align[:, i].count("N") == 0:
#        if align[:, i][0] != align[:, i][1] or align[:, i][1] != align[:, i][2] or align[:, i][0] != align[:, i][2]:
#            sum2 = sum2 + align[:, i:i + 1]
#    elif align[:, i].count("N") == 1:
#        if align[:, i][0] != align[:, i][1] and align[:, i][1] != align[:, i][2] and align[:, i][0] != align[:, i][2]:
#            sum2 = sum2 + align[:, i:i+1]

#SeqIO.write(sum2, "/Users/zhouwenbin/proj/test_beast/50N4.fasta", "fasta")
#print(sum2)

#for i in range(78263):  # inside range is the length of sequence, so is sum2. Should be changed everytime!!

    #	if i + 10 < 1992:
#    if align[:, i].count("N") < 2:
#        sum2 = sum2 + align[:, i:i + 1]
        # print(sum2)
#SeqIO.write(sum2, "/Users/zhouwenbin/proj/test_beast/50N1.fasta", "fasta")


		#	if align2[:, i+2].count("-") > 0:
		#		if align2[:, i+3].count("-") > 0:
		#			if align2[:, i+4].count("-") > 0:
		#				if align2[:, i+5].count("-") > 0:
		#					if align2[:, i+6].count("-") > 0:
		#						if align2[:, i+7].count("-") > 0:
		#							if align2[:, i+8].count("-") > 0:
		#								if align2[:, i+9].count("-") > 0:



#check the length of the alignment
#for record in align:
#		print("%s %i" % (record.id, len(record)))