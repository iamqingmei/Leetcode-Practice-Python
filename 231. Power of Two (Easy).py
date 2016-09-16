"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n): #52 ms
        """
        :type n: int
        :rtype: bool
        """
        while(n>1):
            if (n%2==0):
                n/=2
            else:
                return False

        return (n==1)
    def isPowerOfTwo(self, n): #42 ms
        if (n>=1):
            return (math.pow(2,32)%n==0)
        return False

    def isPowerOfTwo(self,n) :#45 ms
        return n > 0 and not (n & n-1)