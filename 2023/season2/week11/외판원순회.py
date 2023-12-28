# 1번부터 N번까지 번호가 매겨져 있는 도시
# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 순회 여행 경로
# 단, 한 번 갔던 도시로는 다시 갈 수 없다
# 가장 적은 비용이 드는 여행 경로 찾기

N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))

def dfs(start, now, val, cnt): # (시작 도시, 현재 도시, 현재 비용, 방문도시 개수)
    global ans
    if cnt == N: # N개의 도시 모두 방문했다면
        if W[now][start]: # 현재 위치에서 시작 도시로 돌아갈 수 있다면
            val += W[now][start] # 비용 더해주고
            ans = min(ans, val) # 최소비용 업데이트
        return

    if val > ans: # 이미 최소비용을 넘어서면 더이상 볼 필요 X
        return
    
    for i in range(N): # 다른 도시 탐색
        if not visited[i] and W[now][i]: # 방문하지 않은 도시, 현재 위치에서 갈 수 있는 도시이면
            visited[i] = True # 방문 표시
            dfs(start, i, val + W[now][i], cnt + 1) 
            visited[i] = False # 백트래킹 



ans = float('inf')

for i in range(N):
    visited = [False]*N # 각 도시 방문 여부 체크
    visited[i] = True # 방문
    dfs(i, i, 0, 1) # i번째 도시에서부터 시작

print(ans)

### 시간초과 -> visited 배열 대신 비트연산 사용해야함
# https://velog.io/@e_juhee/python-백준-2098-외판원-순회-DP-비트마스킹-lso2bk58
