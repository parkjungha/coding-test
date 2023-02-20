def solution(line):
    stars = []
    for i in range(len(line)):
        for j in range(i+1, len(line)): # 두 직선씩
            a,b,e = line[i]
            c,d,f = line[j]
            if a*d - b*c != 0: # 교점 구하기
                x,y = (b*f - e*d)/(a*d - b*c), (e*c - a*f)/(a*d - b*c)
                if x == int(x) and y == int(y): # 교점이 정수일 경우만
                    if (x,y) not in stars:
                        stars.append((int(x),int(y)))
    
    # 교점들에서 x,y 최대 최소 값 구해서 star matrix 초기화
    x_min, x_max = min(stars)[0], max(stars)[0]
    y_min, y_max = min(stars, key = lambda x: x[1])[1], max(stars, key = lambda x: x[1])[1]
    
    star = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]
    for s in stars: # 별찍기
        a,b = s
        x,y = abs(y_max-b), abs(x_min-a)
        star[x][y] = '*'
        
    for i,v in enumerate(star):
        star[i] = ''.join(v)
                          
    return star

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))