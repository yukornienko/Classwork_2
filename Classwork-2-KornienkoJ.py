
# coding: utf-8

# In[34]:


from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import os
from tqdm import tqdm
os.chdir("/Users/yukornienko/Downloads/BI_spring_2018/Python/KR")

records = []
result_handles = []

with open ("classwork2.fasta") as fasta_in:
    with open ("classwork2_out.fasta", "w") as fasta_out:
        for record in SeqIO.parse(fasta_in, "fasta"):
            print(record)
            result_handle  = NCBIWWW.qblast("blastn", "nt", record.seq)  
            result_handles += [result_handle]
            blast_records = NCBIXML.parse(result_handle)
     
            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        print('sequence:', alignment.title)
                        print('{} ... '.format(hsp.query[0:50]))
                        print('{} ... '.format(hsp.match[0:50]))
                        print('{} ... '.format(hsp.sbjct[0:50]))
                        name = alignment.title
                        break
                    break
                break
            record.name = name
            record.id = name
            SeqIO.write(record, fasta_out, "fasta")
            name = ''

   

#record = SeqIO.read("classwork2.fasta", format="fasta")




with open("blast_result_1.txt", "w") as out_handle:
    for result_handle in result_handles:
        
        out_handle.write(result_handle.read())
    



