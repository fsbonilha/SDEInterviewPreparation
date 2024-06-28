# Problem: Buy and Sell Crypto

# Source: https://neetcode.io/problems/buy-and-sell-crypto

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit
