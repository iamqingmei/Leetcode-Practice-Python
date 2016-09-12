"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution(object):
    def titleToNumber(self, s): #72 ms
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range (len(s)):
            res += (ord(s[len(s) - i - 1]) - 64) * math.pow(26, i)
        return int(res)

# # Get the ASCII number of a character
# number = ord(char)

# # Get the character given by an ASCII number
# char = chr(number)