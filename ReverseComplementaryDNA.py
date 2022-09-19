def ReverseComplement(Pattern):   
    return Complement(Reverse(Pattern))        
    # your code here

# Copy your Reverse() function here.
def Reverse(Pattern):
    reverse = ''
    for char in Pattern:
        reverse = char + reverse
    return reverse
  

# Copy your Complement() function here.
def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement
  
print(ReverseComplement("AAAACCCGGT"))
