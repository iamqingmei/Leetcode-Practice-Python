"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self,n): #42ms
        """
        :type n: int
        :rtype: int
        """
        res=[0]*(n+1)
        return self.climb(n,res)


    def climb(self,n,res):
        if (n>0 and res[n]==0):
            if (n<3):
                res[n]=n
            else:
                res[n] = self.climb(n-2,res) + self.climb(n-1,res)
        return res[n] 