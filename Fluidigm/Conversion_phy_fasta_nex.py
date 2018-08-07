from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os
from Bio import AlignIO


#copy files into one folder.
#path = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus"
#os.mkdir(path)


# mafft

for i in range(51):
    fname1 = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Starbeast/Locus"+str(i) + ".phy"
    fname1_fasta = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Starbeast/fasta/Locus" +str(i) + ".fasta"
    if os.path.isfile(fname1) == True:

        input_handle = open(fname1, "rU")
        output_handle = open(fname1_fasta, "w")

        alignments = AlignIO.parse(input_handle, "phylip")
        AlignIO.write(alignments, output_handle, "fasta")

        output_handle.close()
        input_handle.close()



#transfer the file format
for i in range(51):
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Starbeast/fasta/Locus" +str(i) + ".fasta"
    if os.path.isfile(fname) == True:
        cmd = "python /Users/zhouwenbin/PycharmProjects/Fluidigm/ElConcatenero.py -c -of nexus -in /Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/Starbeast/fasta/Locus" +str(i) + ".fasta"
        os.system(cmd)
