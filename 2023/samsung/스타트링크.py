import sys 

n = int(input())
visited = [0 for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

def dfs(depth, idx):
    global minVal
    if depth == n//2:
        start, link = 0, 0 
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += array[i][j]
                elif not visited[i] and not visited[j]:
                    link += array[i][j]

        minVal = min(minVal, abs(start - link))
        return
    
    for i in range(idx, n):
        if not visited[i]: 
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0
        

minVal = sys.maxsize
dfs(0,0)
print(minVal)