"""
342. Power of Four  
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.
"""
class Solution(object):
    def isPowerOfFour(self, num): #59 ms 30.6%
        """
        :type num: int
        :rtype: bool
        """
        while(num>1):
            if (num%4!=0):
                return False;
            num/=4
        return (num==1)

    def isPowerOfFour(self, num): #52 ms 47%
        """
        :type num: int
        :rtype: bool
        """
        return num >0 and bin(num).count('1')==1 and bin(num)[3:].count('0')%2==0

    