class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq_map = Counter(s)
        
        maxHeap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(maxHeap)

        res = ''

        while len(maxHeap) >= 2:
            fr1, char1 = heapq.heappop(maxHeap)
            fr2, char2 = heapq.heappop(maxHeap)

            res += char1
            res += char2

            if fr1 < -1:
                heapq.heappush(maxHeap, (fr1+1, char1))
            if fr2 < -1:
                heapq.heappush(maxHeap, (fr2+1, char2))
        
        if len(maxHeap) == 1:
            if maxHeap[0][0] < -1:
                return ''
            else:
                fr, char = heapq.heappop(maxHeap)
                res += char
        
        return res
        