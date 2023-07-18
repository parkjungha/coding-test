class Solution:
    # Runtime 58ms (84.48%) Memory 16.63mb (18.62%)
    # Union-Find : 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘
    # 노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산
    
    def equationsPossible(self, equations: List[str]) -> bool:
        parent, diff = {}, []

        # x의 root 찾기 
        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])
        
        # parent 배열 채우기
        for eq in equations:
            a, b = eq[0], eq[3]
            if eq[1] == '=': # 두 숫자(노드) 연결해줌.
                x, y = find(a), find(b) # root 찾기 
                if x != y: 
                    parent[y] = x # x를 y의 부모 노드로 설정

            else: # s[1] == '!': 연결되면 안됨.
                diff.append((a,b))

        # != 인 두 변수 쌍들 중 하나라도 서로 root가 같으면 False, 그렇지 않으면 True  
        return all(find(a) != find(b) for a,b in diff)