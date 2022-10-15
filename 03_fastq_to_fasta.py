from Bio import SeqIO 
count = SeqIO.convert("02_barcode09.fastq", "fastq", "04_barcode09.fasta", "fasta")
print("Converted %i records" % count)
