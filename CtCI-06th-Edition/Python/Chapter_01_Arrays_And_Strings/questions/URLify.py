"""
1.3
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters,and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
", 13
Input:"Mr John "Smith"
Output:"Mr%20John%20Smith"
"""
import unittest
from collections import Counter

def URLify(s:str):
    return s.replace(" ","%20")

s = "Mr John Smith"
print(f"Test Case: {s} Pass ") if URLify(s) == "Mr%20John%20Smith" else print("Fail")