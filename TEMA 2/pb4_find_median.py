import heapq

class MedianFinder:

    def __init__(self):
        
        #numbers from max-heap should be smaller then those in min-heap
        self.max_heap, self.min_heap = [], []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, (-1) * num)

        #check the above condition for the two heaps
        if(self.max_heap and self.min_heap and 
                    (-1) * self.max_heap[0] > self.min_heap[0]):

            val = (-1) * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        #the size of the heaps needs to be balanced
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = (-1) * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = (-1) * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)


    def findMedian(self) -> float:

        if len(self.max_heap) > len(self.min_heap):
            return (-1) * self.max_heap[0]
            
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        else: 
            return ( (-1 * self.max_heap[0]) + self.min_heap[0]) / 2
        
# MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()