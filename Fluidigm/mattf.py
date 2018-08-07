from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os
from Bio import AlignIO


#copy files into one folder.
#path = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus"
#os.mkdir(path)


# mafft


#transfer the file format
for i in range(51):
    fname = "/Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/" + str(i) + ".fasta"
    if os.path.isfile(fname) == True:
        cmd = "python /Users/zhouwenbin/PycharmProjects/Fluidigm/ElConcatenero.py -c -of nexus -in /Users/zhouwenbin/proj/Fluidigm_matrix/Final_sequences/Locus/Matrix/"+str(i)+".fasta"
        os.system(cmd)