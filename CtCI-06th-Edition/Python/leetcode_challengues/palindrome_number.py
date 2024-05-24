'''
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

def palindrome_number(value):
    str_number = f"{value}"
    str_reversed = str_number[::-1]

    print(str_number)
    if str_reversed == str_number:
        return True
    return False

x = input("Introuce a value: ")

print(f"The number introduced is palindrome? {palindrome_number(x)}")
