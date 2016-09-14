"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums): #48ms
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)/2
        dic = {}.fromkeys(set(nums),0)
        for i in range (len(nums)):
            dic[nums[i]]+=1
            if (dic[nums[i]]>n):
                return nums[i]


    def majorityElement(self, nums): #65ms
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)/2
        for i in set(nums):
            if (nums.count(i)>n):
                return i