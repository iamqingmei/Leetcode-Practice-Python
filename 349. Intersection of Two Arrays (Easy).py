"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2): #42 ms
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        res=set()
        while ((i<len(nums1)) & (j<len(nums2))):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else: #nums1[i]==nums2[j]
                res.add(nums1[i])
                i+=1
                j+=1
        return list(res)