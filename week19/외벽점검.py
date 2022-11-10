# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 
from itertools import permutations

def solution(n, weak, dist):
    leng = len(weak) # 취약지점 개수
    for i in range(leng): # 원형 모양의 외벽을 펼친다 -> 배열을 두배로 늘려서
        weak.append(weak[i] + n) # weak 배열에 원소 길이 n을 더해준다
        
    answer = len(dist) + 1 # 투입 가능한 친구의 수(최대값) + 1
    
    for start in range(leng): # 취약점 어디서부터 출발할지 순회
        for friends in list(permutations(dist, len(dist))): # 친구 배열은 모든 경우의 수를 봐야함 
            cnt = 1 # 투입할 친구 수 
            position = weak[start] + friends[cnt-1] # 현재 친구가 점검 가능한 위치 
            
            for idx in range(start, start + leng): # 시작점부터 모든 취약점 확인 
                if position < weak[idx]: 
                    cnt += 1 # 한칸씩 이동한다
                    if cnt > len(dist): # 더 이상 투입할 수 없다면 종료
                        break 
                    position = weak[idx] + friends[cnt-1] # 현재 친구가 점검 가능한 곳 위치 갱신
            answer = min(answer, cnt) # 최소값만 갱신
            
    if answer > len(dist):
        return -1
    
    return answer
    