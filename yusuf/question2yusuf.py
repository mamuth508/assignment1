"""
Question 2
	Please assign variables to the individual components of your favorite gene! (e.g.
	promoter, 5' UTR, start codon, exon1, intron, exon2, stop codon, 3' UTR).
	Print the entire gene by using the string concatenation operator,
	on the standard output! Note: Feel free to create a fictional gene
	sequence by randomly filling in the gene components by the characters
	corresponding to individual nucleotide bases.
"""

promoter = "ATTGCTGCGTTTATT"
UTR5 = "ATCATGCTGATGCAGTGATGCAGTCAGTCGATCGACGTGGCTGTCGATCGAT"
start_codon= "ATG"
exon1="CCACACACATT"
intron1="AGGTCTCG"
stop_codon="TAA"
UTR3 = "GGGGGGGTGTAGTGATGCTGTGATG"
terminator= "TTTGAGAGAGGTTTCCTGCGCGTATTATTAA"

print(promoter + UTR5 + start_codon + exon1 + intron1
      exon1 + "TTTATA" + stop_codon + UTR3 + terminator)
