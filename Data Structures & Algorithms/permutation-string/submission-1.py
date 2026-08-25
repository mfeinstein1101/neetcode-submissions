class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window_size = len(s1)
        target = Counter(s1)
        cur = Counter(s2[:window_size])

        if target == cur:
            return True
        
        for i in range(window_size, len(s2)):
            cur[s2[i-window_size]] -= 1
            cur[s2[i]] = 1 + cur.get(s2[i], 0)

            if target == cur:
                return True
        return False