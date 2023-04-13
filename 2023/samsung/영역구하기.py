
m,n,k = map(int,input().split())
array = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            array[y][x] = 1

count = []
