class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1
        
        heap = [(-freq, n) for n, freq in count.items()]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            freq, n = heapq.heappop(heap)
            res.append(n)

        return res