"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s): #68ms
        """
        :type s: str
        :rtype: int
        """
        
        rlist = []
        for i in "qwertyuiopasdfghjklzxcvbnm":
            if (s.count(i) == 1):
                rlist.append(s.index(i))
                
        if (rlist):
            return min(rlist)
        return -1