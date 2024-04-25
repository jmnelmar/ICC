"""
1.5
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
-> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
pale,
ple
Hints:#23, #97, #130
"""
# O(N)
import time
import unittest

from collections import Counter
def one_way(s:str, t:str):
    if abs(len(t) - len(s)) > 1:
        return False

    discrepancy = 0
    lenn = max(len(t),len(s))

    for i in range(lenn):
        aux1 = s[i] if i < len(s) else None
        aux2 = t[i] if i < len(t) else None

        if aux1 is None and aux2 is not None:
            discrepancy += 1
        elif aux2 is None and aux1 is not None:
            discrepancy += 1
        elif aux1 != aux2:
            discrepancy += 1
    
    if discrepancy > 1:
        return False

    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [one_way]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()