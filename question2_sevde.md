# __CMB1 Group Project__
### Student 1's Answer to Question 2
**Question2:**
Please assign variables to the individual components of your favorite gene! (e.g.promoter, 5’ UTR, start codon, exon1, intron,
exon2, stop codon, 3’ UTR). Print the entire gene by using the string concatenationoperator, on the standard output!
Note: Feel free to create a fictional gene sequence by randomly filling in the genecomponents by the characters
corresponding to individual nucleotide bases.


**My Answer:**
```
promoter_comp = 'GGAATAGCCGACT'
five_UTR_comp = 'CCACGCGTAGCA'
start_codon_comp = 'AUG'
exon1_comp = 'AACCGATCGTAG'
intron1_comp = 'CCACAAG'
exon2_comp = 'AACGTCCACGTCAGC'
intron2_comp = 'CTCGATCGA'
exon3_comp = 'AACAGTGACTGAC'
stop_codon_comp = 'UAA'
three_UTR_comp = 'CCGACGTGAG'

my_fav_gene = promoter_comp + five_UTR_comp + start_codon_comp + exon1_comp + intron1_comp + exon2_comp + intron2_comp + exon3_comp + stop_codon_comp + three_UTR_comp

print(my_fav_gene)
```
