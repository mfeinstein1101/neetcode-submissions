class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(i, cur, cur_val):
            if cur_val == 0:
                ans.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if cur_val - nums[j] < 0:
                    return
                cur.append(nums[j])
                backtrack(j, cur, cur_val - nums[j])
                cur.pop()
        
        backtrack(0, [], target)
        return ans

