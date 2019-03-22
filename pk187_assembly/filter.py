from Bio import SeqIO

NCONTIG_ANALYSED = list(range(23, 31))

records = list(SeqIO.parse('../data/sequenced_variicola.gbk', "gb"))
print(NCONTIG_ANALYSED)  # first record

output_ncontigs = []
for i in range(len(records)):  # Loop through contigs
    ncontig = records[i].id.split('_')[1]  # Get contig number
    if int(ncontig) in NCONTIG_ANALYSED:  # Output only if
        output_ncontigs.append(records[i])

SeqIO.write(output_ncontigs, "NODES_23-30.fasta", "fasta")
