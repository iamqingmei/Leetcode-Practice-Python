# 400. Nth Digit
"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution(object):
    def findNthDigit(self, n): #49 ms
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        sum = digit*9*math.pow(10,digit-1)
        while(n>sum):
            digit+=1
            sum+=digit*9*math.pow(10,digit-1)
        pre = n-(sum-digit*9*math.pow(10,digit-1))
        
        remainder = int(pre%digit)
        baseNumber = int(math.pow(10,digit-1) - 1 + math.floor(pre/digit))
        
        if (remainder>0):
            baseNumber+=1
            digit = len(str(baseNumber))
            return int(baseNumber/math.pow(10,digit-remainder))%10
            
        return int(baseNumber%10)

