'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''

def longestCommonPrefix( strs ) -> str:
    common=""
    new_length = 0
    if len(strs) < 2:
        return ""

    prefix = strs[0]
 
    for i in range(1,len(strs)):
        match = False
        if len(prefix) > len(strs[i]):
            new_length = abs(len(prefix) - len(strs[i]))
        else:
            new_length = len(prefix) 

        while new_length >= 0:
            prefix = prefix[:new_length + 1]
            if prefix ==  strs[i][:new_length + 1]:
                match = True
                break
            else:
                new_length -= 1
        if match:
            common = prefix
        else:
            return ""
    return common

strings = ["hola","hoja","holla"]

print(longestCommonPrefix(strings))