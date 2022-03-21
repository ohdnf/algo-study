class Solution:
    """
    Runtime: 60 ms, faster than 95.04% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    Memory Usage: 15.2 MB, less than 64.94% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                profit += prices[idx] - prices[idx - 1]
        return profit
