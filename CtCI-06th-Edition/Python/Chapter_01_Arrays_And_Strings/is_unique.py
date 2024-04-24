"""
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #7 7 7, #732
"""
from ../tests import Test
from collections import Counter
#Hasmap approach TC O(n) SC: O(n)
def is_unique(s:str):
    map_characters = Counter(s)
    for key in map_characters.keys():
        if map_characters[key] > 1:
            return False
    return True
"""
using set, set ds only allows unique values, if the len of the set is equal to the len of the string 
the string does not have duplicate values
"""
def is_unique_set(s:str):
    return len(set(s)) == len(s)

"""
Two loops TC O(N^2)
"""
def is_unique_II(s:str):
    for i in range(len(s) - 1):
        for j in range(i + 1,len(s)):
            if s[i] == s[j]:
                return False
    return True    

#Sroting apporach TC O(nlogn)
def is_unique_sorting(s:str):
    sorted_string = sorted(s)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique,
        is_unique_set,
        is_unique_II,
        is_unique_sorting
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()

