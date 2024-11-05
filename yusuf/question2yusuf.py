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
5_UTR = "ATCATGCTGATGCAGTGATGCAGTCAGTCGATCGACGTGGCTGTCGATCGAT"
start_codon= "ATG"
exon1="CCACACACATT"
intron1="AGGTCTCG"
stop_codon="TAA"
3_UTR = "GGGGGGGTGTAGTGATGCTGTGATG"
terminator= "TTTGAGAGAGGTTTCCTGCGCGTATTATTAA"

print(promoter + 5_UTR + start_codon + exon1 + intron1
      exon1 + "TTTATA" + stop_codon + 3_UTR + terminator)
