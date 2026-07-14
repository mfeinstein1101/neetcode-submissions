class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suf, ans = [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
            suf[n-i-1] = suf[n-i]*nums[n-i]
        
        ans[0], ans[n-1] = suf[0], pref[n-1]

        for i in range(1, n-1):
            ans[i] = pref[i] * suf[i]
        
        return ans