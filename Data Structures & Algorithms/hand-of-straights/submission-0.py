class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        freq = Counter(hand)
        
        for num in hand:
            if freq[num]:
                for i in range(0, groupSize):
                    if not freq[num+i]:
                        return False
                    freq[num+i] -= 1
        return True
                    