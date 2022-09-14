# 순열 (TC7: 68.03ms)
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons,len(dungeons)):
        temp = k
        cnt = 0
        for i in p:
            if temp >= i[0]: # 최소피로도 조건 만족 -> 탐험 가능
                temp -= i[1] # 탐험 완
                cnt += 1
        answer = max(cnt, answer)
    return answer

# 백트래킹 DFS (TC7: 15.46ms 훨씬 빠름)
answer = 0
def dfs(k,cnt,dungeons,visited):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [0]*len(dungeons)
    dfs(k,0,dungeons,visited)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))