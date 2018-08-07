from Bio import SeqIO

filename = "/Users/zhouwenbin/proj/Xiang/gbe_data/all.fasta"
num_lines = sum(1 for line in open(filename))
for test in SeqIO.parse(filename,'fasta'):
    if "Arabidopsis_thaliana" in test.id:
        file = "/Users/zhouwenbin/proj/Xiang/gbe_data/Arabidopsis2.fasta"
        f1 = open(file, 'a')
        SeqIO.write(test, f1, "fasta")
        f1.close()
