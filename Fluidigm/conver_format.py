from Bio import SeqIO
from Bio import AlignIO
AlignIO.convert("/Users/zhouwenbin/Desktop/ML_tree/No_cp_fungi/Castanea/M50_3.fasta", "fasta", "/Users/zhouwenbin/Desktop/ML_tree/No_cp_fungi/Castanea/M50_3.nexus", "nex")
#with open("/Users/zhouwenbin/PycharmProjects/Fluidigm/Locus3/phy/Locus2.fasta", "rU") as input_handle:
#    with open("/Users/zhouwenbin/PycharmProjects/Fluidigm/Locus3/phy/Locus2.nexus", "w") as output_handle:
#        sequences = SeqIO.parse(input_handle, "fasta")
#        count = SeqIO.write(sequences, output_handle, "nexus")

#print("Converted %i records" % count)

#alignments = AlignIO.parse("/Users/zhouwenbin/Desktop/ML_tree/No_cp_fungi/Castanea/M50_3.phy", "phylip")
#AlignIO.write(alignments, "/Users/zhouwenbin/Desktop/ML_tree/No_cp_fungi/Castanea/M50_3.fasta", "fasta")