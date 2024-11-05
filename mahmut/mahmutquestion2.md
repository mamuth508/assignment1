# Mahmut's Answer to Question 2

**Q2.** Assign variables to the individual components of your favorite gene (e.g
promoter, 5' UTR, start codon, exon1, intron, exon2, stop codon, 3' UTR). Print the
entire gene by using the string concatenation operator on the standard output! Note:
Feel free to create a fictional gene sequence by randomly filling in the components.

```
promoter = "TAATTTAAAATTATATATAAAT"
5_prime_UTR = "GGCAAATTTGATCATTAT"
start_codon = "ATG"
1exon = "CTAGGGTTTTAGCGTAAA"
intron = "GTAGTACCGGGTTAAGGC"
2exon = "CCAGGTTTTCCCAGGTTCAAGGCT"
stop_codon = TGA
3_prime_UTR = "CGATTTAAAAAAGGGCAA"

my_random_gene = promoter + 5_prime_UTR + start_codon + 1exon + \
                 intron + 2exon + stop_codon + 3_prime_UTR
print("My randomized gene sequence is as follows :")
print(my_random_gene)
```


