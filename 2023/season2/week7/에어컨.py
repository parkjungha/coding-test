# 승객이 탑승 중일 때 실내 온도 t1도 이상 t2도 이하 유지

# 1. 에어컨 ON, 실내온도를 1도 변경 : 전력 a 소비
# 2. 에어컨 ON, 온도 유지 : 전력 b 소비
# 3. 에어컨 OFF, 실내온도 1도 변경 : 전력 0 소비
# 4. 에어컨 OFF, 실내온도 유지 (실내온도 == 실외온도인 경우) : 전력 0 소비
# 현재 온도가 변할 수 있는 범위는 min(t1, 실외온도) ~ max(t2, 실외온도)

# 최소 소비전력을 return 

def solution(temperature, t1, t2, a, b, onboard):
    # 온도의 범위가 -10~40도기 때문에, 전부다 10도 씩 올려서 양수로 만듦
    temperature += 10
    t1 += 10
    t2 += 10
    maxV = 1000*100 # (최대 분 * 최대 1분당 소비 전력)
       
    # DP[i][j] = i분에 j 온도 만들 수 있는 최소 소비 전력
    dp = [[maxV]*51 for _ in range(len(onboard))] # -10도부터 40도까지니까 51개의 온도
    dp[0][temperature] = 0
    
    # 에어컨을 켰을 때 온도가 변하는 방향
    if temperature < t1: flag = 1 # 실외온도가 t1보다 낮으면 에어컨 켜서 온도 상승
    if temperature > t2: flag = -1 # 실외온도가 t2보다 높으면 에어컨 켜서 온도 하강
         
    for i in range(1, len(onboard)): # i분        
        for j in range(51): # j도
            tmp = []
            
            if (onboard[i] and t1 <= j <= t2) or not onboard[i]: 
                if 0 <= j - flag <= 50: # 1. 에어컨 켰을 때 실내온도가 (+flag만큼) 변경 되는 경우
                    tmp.append(dp[i-1][j-flag] + a)
                    
                if t1 <= j <= t2: # 2. 에어컨 켰을 때 온도 변하지 않는 경우 (현재 온도 == 희망 온도 범위)
                    tmp.append(dp[i-1][j] + b)       
                    
                if 0 <= j + flag <= 50: # 에어컨 껐을 때 실내온도 (-flag만큼) 변경 되는 경우
                    tmp.append(dp[i-1][j+flag])
                    
                if j == temperature: # 에어컨 껐을 때 온도 변하지 않는 경우 (현재 온도 == 실외 온도)
                    tmp.append(dp[i-1][j])
                    
                dp[i][j] = min(tmp) # 4가지 경우에서 전력이 가장 적은 값
                        
    answer = min(dp[len(onboard)-1])
    return answer