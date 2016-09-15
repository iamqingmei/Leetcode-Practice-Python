"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""
# I -> 1
# V -> 5
# X -> 10
# I -> 50 
# C -> 100
# D -> 500
# N -> 1000
class Solution(object):
    def romanToInt(self, s): #132ms
        """
        :type s: str
        :rtype: int
        """
        romDic={'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        res = romDic[s[-1]]
        
        for i in range(len(s)-1):
            if (romDic[s[i]] < romDic[s[i+1]]):
                res -= romDic[s[i]]
            else:
                res += romDic[s[i]]
        return res


    def romanToInt(self, s): #92
        """
        :type s: str
        :rtype: int
        """
        romDic={'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        res = 0
        previous = 0
        for i in s[::-1]:
            cur = romDic[i]
            if (cur < previous):
                res -= cur
            else:
                res += cur
            previous = cur
        return res
