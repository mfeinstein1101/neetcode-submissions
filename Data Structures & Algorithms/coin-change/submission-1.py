class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        INF = 2**31-1
        dp = [INF] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            min_val = INF
            for c in coins:
                if amt-c >= 0:
                    min_val = min(min_val, 1+dp[amt-c])
            dp[amt] = min_val

        print(dp)
        
        return dp[amt] if dp[amt] != INF else -1