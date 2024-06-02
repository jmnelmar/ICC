'''
5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

def longestPalindrome(s: str) -> str:
    left, right, longest, maxx, substr = 0, 1, "", 0, ""
    
    while left < len(s):
        substr = s[left:right]
        print(f"{left} {right}")
        if substr == substr[::-1]:
            if maxx < len(substr):
                longest = substr
                maxx = len(substr)
        
        if right > len(s) - 1:
            left += 1
            right = left + 1
        right += 1
    return longest

s = "bb"
longest = longestPalindrome(s)
print(longest)