"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""

# https://en.wikipedia.org/wiki/Digital_root
# for reference

# works on python 3.0+

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num - 9* int((num-1)/9)