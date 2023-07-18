class Solution:
    # Run 446ms Mem 23.52mb
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbors = defaultdict(set)
        for a,b in paths: # undirected graph 생성
            neighbors[a].add(b)
            neighbors[b].add(a)

        ans = [0]*n

        for i in range(1, n+1): # 1번째 garden부터 n번째 garden까지 
            available = {1,2,3,4} # 가능한 flower type
            for neighbor in neighbors[i]: # 연결된 garden은 서로 다른 type을 가져야함
                if ans[neighbor-1] in available:
                    available.remove(ans[neighbor-1]) # 이웃과 동일한 type 제거해줌

            ans[i-1] = available.pop() # 남는거중에 하나 넣어줌

        return ans