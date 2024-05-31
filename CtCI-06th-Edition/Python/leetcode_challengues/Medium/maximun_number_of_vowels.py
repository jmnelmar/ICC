'''
in a string of size k problem:
we have a string s, and we want to find 
the maximun number of vowels in a substring
of size k, a substring is a contiguos part of a string

example
s = "bacacbefaobeacfe"
k = 5

output = 4
explanation: we have a substring of size kwith 4 vowels (aobea)
'''
def numberOfVowelsInASubstring(s, k):
    vowels = "aeiouAEIOU"
    maxx = 0
    
    for i in range(len(s) - 1 - (k-1)):
        count = 0
        for c in s[i:(k)+i]:
            if c in vowels:
                count += 1
            maxx = max(maxx,count)
    return maxx

s = "bacacbefaobeacfe"
print(numberOfVowelsInASubstring(s,5))