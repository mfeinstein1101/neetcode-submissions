class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen = 0, 0
        unique = {}
        for r in range(len(s)):
            while s[r] in unique:
                unique.pop(s[l])
                l += 1
            unique[s[r]] = 1
            maxLen = max(maxLen, r-l+1)
        return maxLen