from Bio import SeqIO
from Bio.Seq import Seq
import os


for i in range(48):
    for j in range(48):
        filename = "/Users/xianglab/proj/fluidigm/Individual_result/Ind" +str(i+1) + "/Locus" +str(j+1) +"_con.fq"
        Locusname = "Ind" +str(i+1) + "/Locus" +str(j+1)
        num_lines = sum(1 for line in open(filename))
        if num_lines != 2:
            for test in SeqIO.parse(filename,'fastq'):
        #print test.description
                test.id = Locusname
                file = "/Users/xianglab/proj/fluidigm/Matrix_per_Locus/Locus" +str(j+1) +"_matrix.fasta"
                f1 = open(file, 'a')
                SeqIO.write(test, f1, "fasta")
                f1.close()


# change the name
# conbine the files
for i in range(8):
    for j in range(48):
        filename = "/Users/xianglab/proj/fluidigm/Individual_result/Ind" +str(i+49) + "/Locus" +str(j+1)
        Locusname = "Ind" +str(i+49) + "/Locus" +str(j+1)
        for test in SeqIO.parse(filename,'fasta'):
        #print test.description
            test.id = Locusname
            file = "/Users/xianglab/proj/fluidigm/Matrix_per_Locus/Locus" +str(j+1) +"_matrix.fasta"
            f1 = open(file, 'a')
            SeqIO.write(test, f1, "fasta")
            f1.close()
