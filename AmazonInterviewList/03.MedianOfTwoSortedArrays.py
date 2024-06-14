# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=954v5ops

# Problem: Median of Two Sorted Arrays of size m and n

# Complexity Required: O(log(m + n))

# First Solution --> Complexity O(m + n)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged = []
        size1 = len(nums1) 
        size2 = len(nums2)
        while (i < size1) and (j < size2):
            if (nums1[i] <= nums2[j]):
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while (i < size1):
            merged.append(nums1[i])
            i += 1
        while (j < size2):
            merged.append(nums2[j])
            j += 1

        if (size1 + size2) % 2 == 0:
            pos = (size1 + size2)//2
            return (merged[pos-1] + merged[pos])/2
        else:
            pos = (size1 + size2)//2
            return merged[pos]
        

