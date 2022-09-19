# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    reverse = ''
    for char in Pattern:
        reverse = char + reverse
    return reverse
        
    # your code here

print(Reverse("AAAACCCGGT"))

