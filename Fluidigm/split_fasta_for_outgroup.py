# for fluidigm sequencing.
from Bio import SeqIO
from Bio.Seq import Seq
import os

path = "/Users/xianglab/proj/fluidigm/Per_locus/Camptotheca/"
os.mkdir(path)

filename = "/Users/xianglab/Tools/ncbi-blast/outgroup/camptotheca_output_cds/Hit_sequence_CAMP.fasta"

sum = 0
for test in SeqIO.parse(filename,'fasta'):
	#print test.description
    file = "/Users/xianglab/proj/fluidigm/Per_locus/Camptotheca/Locus" +str(sum+1)
    sum = sum + 1
    f1 = open(file, 'w')
    SeqIO.write(test, f1, "fasta")
    f1.close()