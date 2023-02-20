def solution(triangle):

    # 위에서 아래로 한 단계씩 내려가면서 최대 값 더해주며 업데이트
      
    for i in range(1, len(triangle)): # 두번째줄부터 끝까지
        for j in range(i+1):
            if j == 0: # 맨 왼쪽 모서리일 경우 
                triangle[i][j] += triangle[i-1][0]
            elif i == j: # 맨 오른쪽 모서리인 경우
                triangle[i][j] += triangle[i-1][j-1]
            else: # 중간 값인 경우 위에 두개중에 최대값으로 선택
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    return max(triangle[-1]) # 업데이트 다 끝난 후 맨 밑줄에서 최대값 구하기 

