'''
2063. Vowels of All Substrings
Medium
Topics
Companies
Hint
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring 
of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during 
the calculations.

 

Example 1:

Input: word = "aba"
Output: 6
Explanation: 
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6. 
Example 2:

Input: word = "abc"
Output: 3
Explanation: 
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
Example 3:

Input: word = "ltcd"
Output: 0
Explanation: There are no vowels in any substring of "ltcd".
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters.
'''
def countVowels( word: str) -> int:
    substr = ""
    vowels = "aeiou"
    vowelCount = 0
    left, right = 0, 0

    while left < len(word):
        for c in word[left:right+1]:
            if c in vowels:
                vowelCount += 1
        right += 1
        if right > len(word) - 1:
            left += 1
            right = left

    return vowelCount

def countVowelsII(word:str) -> int:
    ''' Explanation
        For each vowels s[i],
        it could be in the substring starting at s[x] and ending at s[y],
        where 0 <= x <= i and i <= y < n,
        that is (i + 1) choices for x and (n - i) choices for y.

        So there are (i + 1) * (n - i) substrings containing s[i].
    '''
    return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')

def countVowelsIII(word:str) -> int:
    count = 0
    for i, c in enumerate(word):
        if c in "aeiou":
            print(f"i{i}, n:{len(word)-i}")
            count += (i + 1) * (len(word) - i)
            
    return count
    #return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')

word = "aba"
print(countVowelsIII(word))



'''print(countVowels(word))
word = "abc"
print(countVowels(word))
word = "ltcd"
print(countVowels(word))'''

#return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'aeiou')

'''
Detailed explanation
Let us understand this problem with an example
let word = "abei"
All possible substrings:

a        b       e      i
ab       be      ei
abe      bei
abei

So for counting occurences of vowels in each substring, we can count the occurence of each vowel 
in each substring. In this example, count of vowels in substrings are

a - 4 times
e - 6 times
i - 4 times

And you can observe that occurence of each vowel depends on it's position like below:

a is at position 0 so it can be present only in the substrings starting at 0
e is in the middle so it can be present in the substrings starting at it's position, 
substrings ending at it's position, and substrings containing it in middle
i is at last so it can be present only in the substrings ending at that position
Did you see any pattern ? Yes !

A character at position pos can be present in substrings starting at i and substrings ending at j,
where 0 <= i <= pos (pos + 1 choices) and pos <= j <= len (len - pos choices)
so there are total (len - pos) * (pos + 1) substrings that contain the character word[pos]

(You can see from above example that e is at position 2 and it's present in substrings "abei", "bei", "ei", "abe", "be", "e"
(0 <= start <= pos and pos <= end <= len) and same will be true for each vowel.


From this observation we can generalise the occurence of each vowel in the string as

here len(abei) = 4
a,  pos = 0, count = (4 - 0) * (0 + 1) = 4
e,  pos = 2, count = (4 - 2) * (2 + 1) = 6
i,  pos = 3, count = (4 - 3) * (3 + 1) = 4
So the generalised formula will be

count = (len - pos) * (pos + 1)
and we can keep summing the count of each vowel (don't forget to convert to long)
'''

'''
aba n = 3 fixed length = 2
substrings: a ab aba b ba a
aba
positions:
a  => ( 0 + 1 )*( 3 - 0 ) => 1*3 = 3 
0

b => No vowels
1

a => (2 + 1)*(3 - 2) => 3*1 = 3
2

sum = 6
(i+1)*(n-i)

'''