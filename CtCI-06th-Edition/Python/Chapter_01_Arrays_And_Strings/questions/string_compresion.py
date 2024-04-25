"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110
"""
import time
import unittest
import pytest
#sliding window aproach O(n)
def string_compression(s:str):
    left, right = 0,0
    result =""
    chr_count = 0
    chr_count = 1
    if len(s) <= 1:
        return s

    while left < len(s) and right < len(s):        
        if left != right:
            if s[left] == s[right]:
                chr_count += 1
            else:
                result += s[left] + str(chr_count)
                chr_count =1
                left = right
            right +=1
        else:
            right += 1
    result += s[left] + str(chr_count)
    return result if len(result) < len(s) else s

@pytest.mark.parametrize("value, expected",
    [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
        ("aaaaaaaaaaaaaa", "a14")
    ]
)
def test_string_compressionII(value, expected):
    assert string_compression(value) == expected
