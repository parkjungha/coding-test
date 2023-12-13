# https://www.acmicpc.net/problem/1039

from collections import deque

N, K = map(int, input().split())
M = len(str(N))

def bfs(N, K):
    visited = set()
    visited.add((N, 0)) # 바꾼 값, 총 교체 횟수
    q = deque()
    q.append((N, 0))
    answer = 0

    while q:
        n, k = q.popleft()

        if k == K: # 변경 횟수가 K일때
            answer = max(answer, n) # 최대값 갱신
            continue

        n = list(str(n)) 
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and n[j] == '0': # 바꿀 수 없는 경우
                    continue

                n[i], n[j] = n[j], n[i] # 숫자 교환
                swappedN = int(''.join(n)) 

                if (swappedN, k+1) not in visited: # 방문 체크
                    q.append((swappedN, k+1))
                    visited.add((swappedN, k+1))

                n[i], n[j] = n[j], n[i] # 원복

    return answer if answer else -1

print(bfs(N, K))

#https://westmino.tistory.com/87