"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""

class Solution(object):
    def reverseVowels(self, s): #79ms 88.6%
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aieouAIEOU")
        s=list(s)
        low=0
        high=len(s)-1
        while(high>low):
            while(low<high and (s[low] not in vowels)):
                low+=1
            while(low<high and (s[high] not in vowels)):
                high -=1
            
            s[low],s[high]=s[high],s[low]
            low+=1
            high-=1
        return ''.join(s)