class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxProf = 0, 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxProf = max(prof, maxProf)
            else:
                l = r
        return maxProf