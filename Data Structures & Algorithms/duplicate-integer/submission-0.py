class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for num in nums:
            if num in exists:
                return True
            else:
                exists[num] = 1
        return False