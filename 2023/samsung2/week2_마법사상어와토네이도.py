N = int(input())
graph = []
ans = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))

x,y = N//2, N//2

dx = [0,1,0,-1]
dy = [-1,0,1,0]

step = []
for i in range(1,N):
    for _ in range(2):
        step.append(i)
step.append(N-1)

left = [(0,-2,0.05),(-1,-1,0.1),(0,-1,0),(1,-1,0.1),(-2,0,0.02),(-1,0,0.07),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01)]
right = [(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(-x,y,z) for x,y,z in down]

dirs = [[],[],[],[]]
dirs[0],dirs[1],dirs[2],dirs[3] = left, down, right, up

d = 0
for n in range(len(step)):
    for _ in range(step[n]):
        nx, ny = x+dx[d], y+dy[d] # 이동할 칸 
        print([nx,ny])
        for s in range(10): # 모래 퍼짐
            spreads = 0
            nxx = nx + dirs[d][s][0] 
            nyy = ny + dirs[d][s][1]
            rate = dirs[d][s][2]
            print(nxx,nyy,rate)

            if rate: # 비율칸이라면 퍼지는 모래 양 계산
                sand = int(graph[nx][ny]*rate)
            else: # 알파라면
                sand = graph[nx][ny] - spreads

            if 0<= nxx <N and 0<= nyy <N: # 범위 안
                graph[nxx][nyy] += sand
                

            else: # 범위 벗어나면
                ans += sand
            spreads += sand # 퍼진 모래 누적값
        x, y = nx, ny # 현재 칸 수정

        print(graph)

    d = (d+1)%4 

print(ans)