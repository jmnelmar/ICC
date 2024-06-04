'''
6. Zigzag Conversion
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
import pytest

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rows = [""] * numRows
        
    add = 0
    inc = 1
    for i in s:
        rows[add] += i
        if add == 0:
            inc = 1
        elif add == numRows - 1:
            inc = -1

        add += inc
            
    return "".join(rows)
'''
PAYPALISHIRING

   
0    P   A   H   N
1    A P L S I I G
3    Y   I   R
                                    0 1 2  3
  ARRAY1 [ P, A, H, N ]   INDEXES = 0,4,8,12         => i*4 
                                    0 1 2 3 4  5  6
  ARRAY2[ A,P,L,S,I,I,G ] INDEXES = 1,3,5,7,9,11,13 => i*2 + 1
                                    0 1 2
  ARRAY3[ Y,I,R]          INDEXES = 2,6,10          => i*4 + 2

  INDEXES = 0,4,8,12               step = 0 arr1 = 0 arr2 = 1
  INDEXES = 1,3,5,7,9,11,13
  INDEXES = 2,6,10

'''
def zigzagConvert(word, columns):
    step = 1
    position = 0
    rows = [""]*columns

    for char in word:
        print(rows)
        rows[position] += char
        if position == 0:
            step = 1
        elif position == columns - 1: 
            step = -1
        position += step
        
    return "".join(rows)    


s= ["PAYPALISHIRING"]
k = 3
result = zigzagConvert(s,3) 
print(result)