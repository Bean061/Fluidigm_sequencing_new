import Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import SeqIO
align = AlignIO.read("outgroup_fluidigm.phy", "phylip") # phylip file should be export by software.
#len(align)

# check the number of character "-", if it is great than 0, 
sum2 = align[:,60123:60124]

for i in range(60123):#inside range is the length of sequence, so is sum2. Should be changed everytime!!

#	if i + 10 < 1992:
	if align[:, i].count("N") < 36:
		sum2 = sum2 + align[:, i:i+1]
#print(sum2)

SeqIO.write(sum2, "36N.fasta", "fasta")


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