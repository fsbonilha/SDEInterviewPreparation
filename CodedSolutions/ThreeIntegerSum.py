# Problem: Three Integer Sum

# Source: https://neetcode.io/problems/three-integer-sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        sortedNums = nums.copy()
        sortedNums.sort()
        length = len(sortedNums)

        for index in range(length - 2):
            if sortedNums[index] > 0:
                break
            
            if index > 0 and sortedNums[index] == sortedNums[index - 1]:
                continue

            start = index + 1
            end = length - 1
            while start < end:
                nsum = sortedNums[index] + sortedNums[start] + sortedNums[end]
                if nsum > 0:
                    end -= 1
                elif nsum < 0:
                    start += 1
                else:
                    triplets.append([sortedNums[index], sortedNums[start], sortedNums[end]])
                    start += 1
                    end -= 1
                    while sortedNums[start] == sortedNums[start - 1] and start < end:
                        start += 1
        return triplets