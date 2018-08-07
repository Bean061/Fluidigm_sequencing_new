import os
import subprocess


#for .fai file ####same create index file.
cmd = "samtools faidx /Users/xianglab/proj/fluidigm/Total_REF/Concatenated_sequences.fasta"
os.system(cmd)

#Bowtie2
cmd2 = "bowtie2-build /Users/xianglab/proj/fluidigm/Total_REF/Concatenated_sequences.fasta /Users/xianglab/proj/fluidigm/Total_REF/REF"
os.system(cmd2)

for i in range(48):
	path1 = "/Users/xianglab/proj/fluidigm/Ind" + str(i+1)
	path2 = "/Users/xianglab/proj/fluidigm/Total_REF/Ind" + str(i + 1)
	os.mkdir(path1)
	os.mkdir(path2)

for i in range(48):
	for j in range(48):
		individual = "Ind" + str(i+1) +"/Locus" + str(j+1)
		cmd3 = "bowtie2 -U /Users/xianglab/proj/fluidigm/Per_locus/" + individual +" -x /Users/xianglab/proj/fluidigm/Total_REF/REF > /Users/xianglab/proj/fluidigm/Total_REF/" + individual +".sam"
		os.system(cmd3)

#sort
		cmd4 = "samtools sort -o /Users/xianglab/proj/fluidigm/Total_REF/"+ individual +".sorted.bam /Users/xianglab/proj/fluidigm/Total_REF/"+individual +".sam"
		os.system(cmd4)


#
		cmd5 = "samtools mpileup -uf /Users/xianglab/proj/fluidigm/Total_REF/Concatenated_sequences.fasta /Users/xianglab/proj/fluidigm/Total_REF/"+ individual +".sorted.bam | bcftools call -c | vcfutils.pl vcf2fq > /Users/xianglab/proj/fluidigm/"+ individual + "_con.fq"
		os.system(cmd5)
