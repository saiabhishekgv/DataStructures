'''

Question 4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

'''
Solution : 
    1. Brute Force 
        - Time Complexity : O(m+n)
        - Runtime: 132 ms
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist = self.mergelists(nums1, nums2)
        l = len(newlist)
        if l % 2 != 0:
            return newlist[l / 2]
        else:
            return (newlist[l / 2] + newlist[l / 2 - 1]) / 2.0

    def mergelists(self, nums1, nums2):
        newlist = []
        l1 = len(nums1)
        l2 = len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                newlist.append(nums1[i])
                i += 1
            else:
                newlist.append(nums2[j])
                j += 1

        while i < l1:
            newlist.append(nums1[i])
            i += 1

        while j < l2:
            newlist.append(nums2[j])
            j += 1

        return newlist

