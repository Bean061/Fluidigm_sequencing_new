# This file converts reads in a sam file into fasta formated alignment
# Xiang Ji
# xji3@ncsu.edu

import os
from simplesam import Reader

if __name__ == '__main__':
     sam_file = './Contig.sam'
     sam_iter = Reader(open(sam_file, 'r'))
     fasta_file = sam_file.replace('.sam', '.fasta')

     read = next(sam_iter)
     with open(fasta_file, 'w+') as f:
          while read:
               f.write('>' + read.safename + '\n')
               f.write(read.gapped('seq') + '\n')
               try:
                    read = next(sam_iter)
               except:
                    read = False
               
               
