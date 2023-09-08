class Solution:
    # Min heap 으로 빌딩의 최대 높이 값 찾기 
    # Runtime 45.84% (142ms) Memory 39.31% (22.3MB)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right)) # start point
            events.append((right, 0, 0)) # end point
        events.sort()

        # 우선순위 큐 초기화
        queue = [(0, float('inf'))] # (-height, Right x좌표)
        skyline = []
        prev = 0

        for x, neg_height, right in events:
            while queue and queue[0][1] <= x:
                heapq.heappop(queue) # 지나간 max height 값 제거

            if neg_height: # start point인 경우 heap에 push
                heapq.heappush(queue, (neg_height, right)) # 높이, right 좌표

            cur_height = -queue[0][0] # current max height
            if cur_height != prev: # previous max height과 다르면
                skyline.append([x, cur_height])
                prev = cur_height # 갱신 

        return skyline