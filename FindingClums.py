def FormingClumps(text, patterns, time):
    clumps = {}
    for i in range( len(text)-patterns+1 ):   # Loop all k-mers in Genome
        kmer = text[i:i+patterns]             # Substring k-mer with the lenght k
        if not kmer in clumps:           # If the k-mer is found for the first time, add it to clumps dictionary
            clumps[kmer] = 1
        else:
            clumps[kmer] += 1            # If the k-mer is found for second, third, ... time, increase its number in clumps dictionary
    for c in clumps:                    # Loop all keys in clumps dictionary
        if int(clumps[c]) == time:          # If the number of clumps found in genome is equal to t, print it out
            print(c)
        
text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"
patterns = 9                                    # k-mers 
time = 2                                    # The number of times that k-mers appear in genome
FormingClumps(text, patterns, time)
