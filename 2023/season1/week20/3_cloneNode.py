"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Run 60ms (22.62%) Mem 16.89mb (29.75%)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        visited = {} # cloned된 노드들 저장

        def dfs(node):
            if node in visited: # 이미 방문되었을 경우
                return visited[node] 
            
            clone_node = Node(node.val, []) # new clone node 생성
            visited[node] = clone_node # mapping 해줌

            for neighbor in node.neighbors: # 해당 노드의 모든 이웃 방문
                clone_node.neighbors.append(dfs(neighbor)) # 재귀.

            return clone_node
        
        return dfs(node) # 첫번째 노드부터 DFS 탐색 시작