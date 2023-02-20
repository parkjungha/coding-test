# 다음 인덱스에 해당하는 numbers 원소를 더하거나 뺸 값을 방문한다

def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]] # index값도 queue에 함께 넣어준다
    n = len(numbers)
    while queue:
        temp, idx = queue.pop() 
        idx += 1 # 다음 인덱스 
        if idx < n: 
            queue.append([temp+numbers[idx],idx]) # 더했을 때
            queue.append([temp-numbers[idx], idx]) # 뺐을 때
        else: # pop한게 마지막 원소이고
            if temp == target: # 값이 target과 같다면 
                answer += 1
    return answer