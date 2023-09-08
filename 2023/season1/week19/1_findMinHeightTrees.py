class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set) # 각 노드(key)의 이웃 노드들(value)를 담고 있는 dictionary
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1]) # 이웃 노드가 하나밖에 없는 leaf node들 담는 Queue

        while n > 2: 
            leaf_cnt = len(leaves) # leaf node 개수
            n -= leaf_cnt # total n에서 빼줌
            for i in range(leaf_cnt): # for each leaf node, 
                leaf = leaves.popleft() # Queue에서 빼줌
                neighbor = graph[leaf].pop() # remove the neighbor
                graph[neighbor].remove(leaf) # 양방향 connection 제거
                if len(graph[neighbor]) == 1: # 제거했을 때 neighbor도 leaf node가 되면
                    leaves.append(neighbor) # leaf node담는 Queue에 추가

        # 마지막에 남은 1개 또는 2개의 노드는 min height를 가지는 root가 된다. 
        return list(leaves) # 그것의 index 반환

        