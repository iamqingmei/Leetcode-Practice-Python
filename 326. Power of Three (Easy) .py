"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n): #208
        """
        :type n: int
        :rtype: bool
        """
        while(n>1):
            if (n%3 == 0):
                n/=3
            else:
                return False
        return n==1
    def isPowerOfThree(self, n): #329
        """
        :type n: int
        :rtype: bool
        """
        if (n>=1):
            return (math.pow(3,20)%n==0)
        return False