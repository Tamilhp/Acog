import os.path
import sys
from Bio.Emboss.Applications import NeedleCommandline
from Bio import Entrez
from Bio import SeqIO

# GLOBAL
Entrez.email = "shea.d@husky.neu.edu"

def getFasta(genbank_id):
    filename = '{0:s}.fa'.format(genbank_id)
    if not os.path.isfile(filename):
        handle = Entrez.efetch(db='nucleotide', rettype='fasta', retmode='text', id=genbank_id)
        seq_record = SeqIO.read(handle, 'fasta')
        handle.close()
        SeqIO.write(seq_record, filename, format='fasta')
    return(filename)

def main():
    if len(sys.argv) != 3:
        print('usage {0:s} genbank_id1 genbank_id2'.format(sys.argv[0]))
        sys.exit(1)
    genbank_a = sys.argv[1]
    genbank_b = sys.argv[2]
    sequence_a = getFasta(genbank_a)
    sequence_b = getFasta(genbank_b)
    needle_cline = NeedleCommandline(asequence=sequence_a, bsequence=sequence_b,
                                     gapopen=10, gapextend=1, endweight=True, endopen=10, endextend=1,
                                     outfile='{0:s}_{1:s}_needle.txt'.format(genbank_a,genbank_b))
    stdout, stderr = needle_cline()
    sys.exit(0)

if __name__ == '__main__':
    main()
