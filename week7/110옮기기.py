# 110을 모두 찾아서 가장 왼쪽에 있는 111 앞에 넣는다 
# 110을 삽입한 후에 새로운 111이 발생하지 않도록 string에서 가장 뒤쪽에 있는 0 뒤에 110을 삽입한다.

def solution(s):
    answer = []
    for string in s:
        cnt, idx, stack = 0, 0, ""
        while idx < len(string):
            if string[idx] == "0" and stack[-2:] == "11": # 110 찾기
                stack = stack[:-2]
                cnt += 1
            else:
                stack += string[idx]
            idx += 1
        idx = stack.find("111") # 110이 빠진 string에서 111 찾기
        if idx == -1: # 없다면
            idx = stack.rfind('0') # 가장 뒤쪽에 있는 0의 idx
            stack = stack[:idx+1] + "110"*cnt + stack[idx+1:] #뒤에 110 반복해서 붙이기
        else: # 111 있으면 앞에 110 반복해서 붙이기
            stack = stack[:idx] + "110"*cnt + stack[idx:]
        answer.append(stack)
    return answer

print(solution(["1110","100111100","0111111010"]	))