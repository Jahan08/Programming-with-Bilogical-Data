# Copy your PatternCount function below here
def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# On the following line, create a variable called Text that is equal to the oriC region from T petrophila
Text = "aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga"

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.

Pattern1 = "ATGATCAAG"
count_1=PatternCount(Text, Pattern1)


# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 

Pattern2 = "CTTGATCAT"
count_2=PatternCount(Text, Pattern2)



# Finally, print the sum of count_1 and count_2

Total_count = count_1+count_2

print(Total_count)
