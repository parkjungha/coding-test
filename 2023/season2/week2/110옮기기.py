def solution(s):
    answer = []
    for string in s:
        count, idx, stack = 0, 0, ""
        while idx < len(string): # 110 찾기
            if string[idx] == "0" and stack[-2:] == "11": # 0을 만나면 직전 문자열이 11 인지 확인
                stack = stack[:-2]  # 맞으면 110 제거
                count += 1
            else:
                stack += string[idx]
            idx += 1

        idx = stack.find("111") # 111 찾기 (앞에서부터)
        if idx == -1: # 111이 없다면 
            idx = stack.rfind('0') # 0 찾기 (뒤에서부터)
            stack = stack[:idx+1] + "110"*count + stack[idx+1:] # 제일 뒤의 0 뒤에 110 붙이기
        else: # 111이 있다면 그 앞에 붙임
            stack = stack[:idx] + "110"*count + stack[idx:]
        answer.append(stack)

    return answer
