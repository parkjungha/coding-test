
n, m, k = map(int, input().split())
graph = []
sharks = [[] for _ in range(m + 1)]

# 격자 정보
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] != 0:
            sharks[a[j]].append([i, j]) # [현재 위치, 방향]
    graph.append(a)

# 각 상어의 초기방향
directions = list(map(int, input().split()))

for i in range(1, m + 1):
    sharks[i].append(directions[i - 1])

# 각 상어의 방향 우선순위
priorities = {}
for i in range(1, m + 1):
    priorities[i] = [0]
    for j in range(1, 5):
        priorities[i].append(list(map(int, input().split())))


