class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MIN, MAX = -(2**31), 2**31-1
        neg = (x < 0)
        if neg:
            x *= -1
        while x > 0:
            den = x%10
            res = res*10 + den
            x //= 10
            if not MIN <= res <= MAX:
                return 0
        return res * -1 if neg else res