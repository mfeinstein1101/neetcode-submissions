class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, cur, cur_val):
            if cur_val == 0:
                ans.append(cur.copy())
                return
            elif cur_val < 0 or i == len(nums):
                return
            else:
                cur.append(nums[i])
                backtrack(i, cur, cur_val-nums[i])
                cur.pop()
                backtrack(i+1, cur, cur_val)
        
        backtrack(0, [], target)
        return ans

