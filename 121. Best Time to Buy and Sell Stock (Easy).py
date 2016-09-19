"""
121. Best Time to Buy and Sell Stock (Easy)
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
    def maxProfit(self, prices): #55ms
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices)<2):
            return 0
        low = prices[0]
        high = 0
        profit = 0
        for i in prices:
            if (i<low):
                low = i
            elif (i>low):
                high = i
                curProfit = high - low
                if curProfit > profit:
                    profit = curProfit
        return profit
