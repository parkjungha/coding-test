def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results: # 이긴 쪽은 1, 진 쪽은 0
        matrix[win-1][lose-1] = 1
        matrix[lose-1][win-1] = 0
        
    for i in range(n):
        for j in range(n):
            for k in range(n): # j -> k로 갈 때 i를 거쳐 j -> i -> k로 갈수 있는가
                if matrix[j][i] == None: # j-i 연결 안되있으면 pass
                    continue
                    
                if matrix[j][i] == matrix[i][k]: # 연결 되어 있으면 승부 정보 update
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]
                    
    ans = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i+1:]: # 자기자신 노드 빼고 None이 없어야함.
            continue
        ans += 1
    return ans
