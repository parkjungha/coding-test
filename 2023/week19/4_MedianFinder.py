class MedianFinder_:
# 그냥 list 사용, sort해서 중간값 찾기
# Runtime 5.3% (4124ms) Memory 54.28% (38.3 MB)
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)

        if len(self.arr)%2 == 0:
            mid = len(self.arr)//2
            return (self.arr[mid] + self.arr[mid-1])/2

        else:
            return self.arr[len(self.arr)//2]


import heapq
# Runtime 93.91% (470ms) Memory 42.51% (38.5MB)
class MedianFinder:
    def __init__(self):
        # Two heaps
        self.small = [] # max heap 
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large): # 개수 같으면 small heap의 가장 큰 값 빼서 large heap에 넣고
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else: # 다르면 large headp의 가장 작은 값 빼서 small heap에 넣음 
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else: # smallest element in large heap
            return float(self.large[0])