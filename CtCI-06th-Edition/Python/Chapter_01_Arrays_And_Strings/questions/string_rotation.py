"""
1.9
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
Hints: #34, #88, # 7 04
"""
import pytest
def string_rotation(s:str, t:str):
    string_rotated = ""
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        string_rotated = s[i + 1: len(s)] + s[0:i+1]
        print(string_rotated)
        if string_rotated == t:
            return True
    
    return False

@pytest.mark.parametrize( "value, value2, expected",
    [
         ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
        ("amigo", "igoam", True),
        ("", "igoam", False),
        ("omega", "egoma", False),
        ("girafa", "fagira", True),
        
    ]
)
def test_string_rotation(value, value2, expected):
    assert string_rotation(value, value2) == expected

