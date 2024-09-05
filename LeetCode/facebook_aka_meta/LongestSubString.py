'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
import pytest

def lengthOfLongestSubstring(s: str) -> int:
    right = 0
    left = 0
    maxSubString = 0
    chars = set()

    for right in range( len(s) ):
        while s[ right ] in chars:
            chars.remove(s[left])
            left = left + 1
        
        chars.add(s[right])
        maxSubString = max(maxSubString, right - left + 1)
    
    return maxSubString


def longest(s:str)->int:
    left = 0
    right = 0
    maxstr = 0
    chars = set()

    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left = left + 1
        chars.add(s[right])
        maxstr = max(maxstr, right - left + 1)
    return maxstr           

@pytest.mark.parametrize("value, expected",[
    ("abcabcbb",3),
    ("bbbbb",1),
    ("pwwkew",3)
    ])
def test_lengthOfLongestSubstring(value,expected):
    assert longest(value) == expected
