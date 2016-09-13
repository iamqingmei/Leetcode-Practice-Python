"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution(object):
    def isAnagram(self, s, t): #39 ms
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in "qwertyuiopasdfghjklzxcvbnm":
            if (s.count(i) != t.count(i)):
                return False
        return True
