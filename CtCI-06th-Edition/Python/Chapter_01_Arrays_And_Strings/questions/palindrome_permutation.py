"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input:Tact Coa
Output:True (permutations: "taco cat", "atco eta", etc.)
"""
# O(N)
import string
import unittest
from collections import Counter

def palindrome_permutation(s:str):
    clean = [c for c in s.lower() if c in string.ascii_lowercase]
    map =   Counter(clean)
    return sum(val % 2 for val in map.values() ) <= 1


print("pass") if palindrome_permutation("aba") else print("fail")
print("pass") if palindrome_permutation("aab") else print("fail")
print("pass") if palindrome_permutation("abba") else print("fail")
print("pass") if palindrome_permutation("aabb") else print("fail")
print("pass") if palindrome_permutation("a-bba") else print("fail")
print("pass") if palindrome_permutation("a-bba!") else print("fail")
print("pass") if palindrome_permutation("Tact Coa") else print("fail")
print("pass") if palindrome_permutation("jhsabckuj ahjsbckj") else print("fail")
print("pass") if palindrome_permutation("Able was I ere I saw Elba") else print("fail")
print("pass") if palindrome_permutation("So patient a nurse to nurse a patient so") else print("fail")


"""
class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        palindrome_permutation
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
"""