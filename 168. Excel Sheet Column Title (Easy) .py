"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
class Solution(object):
    def convertToTitle(self, n): #35 ms
        """
        :type n: int
        :rtype: str
        """
        s=''
        while(n>0):
            n-=1
            s+=unichr(65+n%26)
            n/=26
        return s[::-1]

        

# # Get the ASCII number of a character
# number = ord(char)

# # Get the character given by an ASCII number
# char = chr(number)