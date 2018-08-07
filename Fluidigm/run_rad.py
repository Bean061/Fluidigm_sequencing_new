#run pyRAD
#import os
#sum1 = ""
for i in range(51):
    cmd = "curl -O ftp://ftp.ncbi.nlm.nih.gov/refseq/release/fungi/fungi." + str(i+1) + ".1.genomic.fna.gz"
    #sum1 = sum1 + cmd + " "
    print cmd
    #os.system(cmd)
#print sum1