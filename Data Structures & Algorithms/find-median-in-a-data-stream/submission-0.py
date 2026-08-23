class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num <= self.minHeap[0]:
            heapq.heappush(self.maxHeap, num * -1)
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))


    def findMedian(self) -> float:
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (float(self.minHeap[0]) + -1 * float(self.maxHeap[0])) / 2
            
        