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
        - Runtime : 132 ms
    2. Binary Search on Smaller List: 
        - Time Complexity : O(log(min(m,n)))
        - Runtime : 132 ms 
'''

import sys
class Solution(object):
    def findMedianSortedArrays_1(self, nums1, nums2):
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

    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = l1

        while low <= high:

            partition_nums1 = (low + high) / 2
            partition_nums2 = (l1 + l2 + 1) / 2 - partition_nums1

            maxLeft_nums1 = -sys.maxint - 1 if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            minRight_nums1 = sys.maxint if partition_nums1 == l1 else nums1[partition_nums1]

            maxLeft_nums2 = -sys.maxint - 1 if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            minRight_nums2 = sys.maxint if partition_nums2 == l2 else nums2[partition_nums2]

            if maxLeft_nums1 <= minRight_nums2 and maxLeft_nums2 <= minRight_nums1:
                if (l1 + l2) % 2 == 0:
                    return (max(maxLeft_nums1, maxLeft_nums2) + min(minRight_nums1, minRight_nums2)) / 2.0
                else:
                    return max(maxLeft_nums1, maxLeft_nums2)

            elif maxLeft_nums1 > minRight_nums2:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1

        return -1
