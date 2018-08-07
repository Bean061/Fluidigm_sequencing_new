import sys
import os
 #
from Bio import AlignIO
 
s_bases = ('A', 'C', 'G', 'T')
d_bases = ('R', 'Y', 'S', 'W', 'K', 'M', 'N')
bases = s_bases + d_bases
 
deg_map = {'A':('A','A'),'C':('C','C'), 'G':('G','G'), 'T':('T','T'), 'R':('A','G'), 'Y':('C','T'), 'S':('C','G'), 'W':('A','T'), 'K':('G','T'), 'M':('A','C')}
 
alig = AlignIO.read(sys.argv[1], 'fasta')
 
inname = os.path.basename(sys.argv[1])
 
colnames = [sq.id for sq in alig]
colnames = ['file', 'pos'] + colnames
print '\t'.join(colnames)
 
cutoff = 0.5
for i in range(alig.get_alignment_length()):
    col = alig[:,i]
    col = col.upper()
    col = col.replace('-', 'N') 
 
    base_count = {b:col.count(b) for b in bases}
    del base_count['N']
 
    if sum(base_count.values()) > len(col)*cutoff:
 
        genotypes = sorted(base_count.items(), key=lambda x:-x[1])
        genotypes = [b for b in genotypes if b[1] > 0]
 
        ref = genotypes[0][0]
 
        if ref in d_bases:
            ref = deg_map[ref][0]
 
        allel = [deg_map[b[0]] for b in genotypes]
        allel = reduce(lambda x,y: x+y, allel)
        allel = list(set(allel))
 
        j = allel.index(ref)
        allel[0], allel[j] = allel[j], allel[0]
 
        allel_code = {b:k for k, b in enumerate(allel)}
 
        if len(allel) > 1:
            snps = [inname, '%d'%(i+1), ref, ','.join(allel[1:])]
            for s in col:
                if not s == 'N':
                    code = [allel_code[a] for a in deg_map[s]]
                    code = sorted(code)
                    snps.append('%d/%d' % (code[0], code[1]))
 
                else:
                    snps.append('-/-')
            print '\t'.join(snps)