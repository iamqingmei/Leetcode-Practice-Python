"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
def intersect(self, nums1, nums2): #66ms
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    r.append(i)
                    nums1.remove(i)
        else: 
            for i in nums1:
                if i in nums2:
                    r.append(i)
                    nums2.remove(i)
        return r

def intersect(self, nums1, nums2): #52ms

        nums1.sort()
        nums2.sort()
        
        res = []
        
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i + 1, j + 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res

def intersect(self, nums1, nums2): #52ms
        import collections
        
        dict1 = dict(collections.Counter(nums1))
        res = []
        
        for i in nums2:
            if dict1.has_key(i):
                if dict1[i] > 0:
                    dict1[i] -= 1
                    res.append(i)
        
        return res