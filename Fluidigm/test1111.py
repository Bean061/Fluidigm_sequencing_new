import os
import subprocess
#for .fai file ####same create index file.
cmd = "samtools faidx /Users/xianglab/proj/fluidigm/Total_REF/N14_2.fasta"
os.system(cmd)

#Bowtie2
cmd2 = "bowtie2-build /Users/xianglab/proj/fluidigm/Total_REF/N14_2.fasta /Users/xianglab/proj/fluidigm/Total_REF/REF5"
os.system(cmd2)

#for i in range(48):
#	path1 = "/Users/xianglab/proj/fluidigm/Ind" + str(i+1)
#	path2 = "/Users/xianglab/proj/fluidigm/Total_REF/Ind" + str(i + 1)
#	os.mkdir(path1)
#	os.mkdir(path2)

#for i in range(48):
#	for j in range(48):
#		individual = "Ind" + str(i+1) +"/Locus" + str(j+1)
cmd3 = "bowtie2 -U /Users/xianglab/proj/fluidigm/Per_locus/Ind21/Locus10 -x /Users/xianglab/proj/fluidigm/Total_REF/REF5 > /Users/xianglab/proj/fluidigm/test/result/ind21locus10.sam"
os.system(cmd3)

#sort
cmd4 = "samtools sort -o /Users/xianglab/proj/fluidigm/test/result/ind21locus10.sorted.bam /Users/xianglab/proj/fluidigm/test/result/ind21locus10.sam"
os.system(cmd4)


#
cmd5 = "samtools mpileup -uf /Users/xianglab/proj/fluidigm/Total_REF/N14_2.fasta /Users/xianglab/proj/fluidigm/test/result/ind21locus10.sorted.bam | bcftools call -c | vcfutils.pl vcf2fq > /Users/xianglab/proj/fluidigm/test/result_con/N14_2.fq"
os.system(cmd5)



cmd8 = "tabix /Users/xianglab/proj/fluidigm/test/result/calls.vcf.gz"
os.system(cmd8)

cmd7 = "cat /Users/xianglab/proj/fluidigm/Total_REF/N39.fasta | bcftools consensus /Users/xianglab/proj/fluidigm/test/result/calls.vcf.gz > /Users/xianglab/proj/fluidigm/test/result/consensus.fa"
os.system(cmd7)

cmd6 = "samtools mpileup -uf /Users/xianglab/proj/fluidigm/Total_REF/N39.fasta /Users/xianglab/proj/fluidigm/test/result/ind21locus25.sorted.bam | bcftools call -c | vcfutils.pl vcf2fq > /Users/xianglab/proj/fluidigm/test/result_con/N39.fq"
os.system(cmd6)


vcfutils.pl varFilter -d 5 -a 5
vcfutils.pl vcf2fq -d 5


cmd5 = "samtools index Users/xianglab/proj/fluidigm/test/result/ind21locus25.sorted.bam"
os.system(cmd5)
cmd6 = "samtools tview /Users/xianglab/proj/fluidigm/test/result/ind21locus25.sorted.bam /Users/xianglab/proj/fluidigm/Total_REF/N39.fasta"
os.system(cmd6)
