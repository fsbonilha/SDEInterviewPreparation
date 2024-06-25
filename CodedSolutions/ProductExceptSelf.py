# Source: https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero = 1
        for num in nums:
            if num != 0:
                product = product * num
            elif zero == 1:
                zero = 0
            else:
                product = 0
        for num in nums:
            if num != 0:
                productExptCurrent = (product//num)*zero
            else:
                productExptCurrent = product
            result.append(productExptCurrent)
        return result
