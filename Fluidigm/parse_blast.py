import Bio
from Bio import SeqIO
from Bio.Blast import NCBIXML


save_file = open("/Users/xianglab/Tools/ncbi-blast/outgroup/Nyssa_ursina_output/Hit_sequence.fasta", "w")
results = open("/Users/xianglab/Tools/ncbi-blast/outgroup/Nyssa_ursina_output/ursina5.csv", "r")  # Read your output file.
blast_records = NCBIXML.parse(results)
for blast_record in blast_records:
    blast_record
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 0.01:
                #print(hsp.num_alignments)
                #print(dir(hsp))
                #print('****Alignment****')
                #print('sequence:', alignment.accession)
                #print('length:', alignment.length)
                #print('score:', alignment.score)
                #print('gaps:', alignment.gaps)
                #print('e value:', hsp.expect)
                #print(hsp.query[0:90] + '...')
                #print(hsp.match[0:90] + '...')
                #print(hsp.sbjct)
                #print(hsp.hit)
                #print(dir(alignment))
                sum2 = '>' + alignment.accession + '\n' + hsp.sbjct + '\n'
                #sum2 = hsp.sbjct
                #m = m + 1
                #print(sum2)
                #SeqIO.write(sum2, 'Subject' + str(m) + '.fa', 'fasta')
                save_file.write(sum2)

results.close()
save_file.close()
#blast_qresult = SearchIO.parse('output.xml', 'blast-xml')
