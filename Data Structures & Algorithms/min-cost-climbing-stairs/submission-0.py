class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = [0, 0]

        for i in range(2, len(cost)+1):
            cache.append(min(cache[i-2] + cost[i-2], cache[i-1] + cost[i-1]))
        
        return cache[-1]