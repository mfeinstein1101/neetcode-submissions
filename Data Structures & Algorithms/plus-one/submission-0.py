class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + c
            c = 1 if sum >= 10 else 0
            digits[i] = sum % 10
        if c == 1:
            digits.insert(0, 1)
        return digits