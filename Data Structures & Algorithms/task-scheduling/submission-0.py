class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {t: 0 for t in tasks}
        
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        maxHeap = [-fr for fr in freq.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                fr = 1 + heapq.heappop(maxHeap)
                if fr:
                    q.append((fr, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

            
