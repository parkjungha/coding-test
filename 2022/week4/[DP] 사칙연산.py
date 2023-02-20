# 너무 어려움 ㅠㅠ 

# 뒤에서 부터 읽으며 -를 만났을 때에는 최댓값과 최솟값을 갱신하고 +를 만나면 이전 -부터 다음 -까지 숫자를 더해 식을 계산해나가는 방식
# 즉, -SUM(현재 인덱스 ~ 이전 -의 바로 앞 인덱스) + (최대 or 최소)

# [Case 1] a-(b+c-d) : 식 전체에 영향을 미치는 경우 > -(sum + 최대or최소)
# [Case 2] a-(b+c)-d : 다음 -전까지의 식에 영향을 미치는 경우 > -(sum) + 최대or최소
# [Case 3] a-(b)+c-d : -바로 뒤의 숫자에만 영향을 미치는 경우 > -(sum[0]) + sum[1:] + 최대or최소

def solution(arr):
    minmax = [0,0]
    sum_val = 0
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue

        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_val + tempmax), -sum_val + tempmin)
            # -(sum+max): -가 식 전체에 붙는 경우, -sum+min: -가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_val + tempmin), -minus_v + (sum_val - minus_v) + tempmax)
            # -(sum+min): -가 식 전체에 붙는 경우, -v+(sum-v)+max: -가 바로 뒤의 값에만 붙는 경우
            sum_val = 0

        elif int(arr[idx]) >= 0:
            sum_val += int(arr[idx])

    minmax[1] += sum_val
    return minmax[1] # 최대값
        
print(solution(["1", "-", "3", "+", "5", "-", "8"]))