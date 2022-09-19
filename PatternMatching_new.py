# Apply your solution to the Pattern Matching Problem to find all starting positions of "CTTGATCAT" in the Vibrio cholerae genome. 

# Copy your PatternMatching function below this line.
def PatternMatching (Pattern,Genome):
    positions = [] # output variable
    Gen= len(Genome)
    Pat= len(Pattern)
    # your code here
    for occurrence in range (Gen - Pat +1):
        if Pattern == Genome [occurrence : occurrence + Pat] :
            positions.append(occurrence)
    return positions
# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'

# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
positions= PatternMatching ("CTTGATCAT",v_cholerae) # we put the input data here

# print the positions variable
print (positions)
