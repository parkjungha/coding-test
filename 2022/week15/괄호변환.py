def divide(p): # p를 u와 v로 분리한다
    cnt = [0,0]
    for i in range(len(p)):
        if p[i] == '(':
            cnt[0] += 1
        else: cnt[1] += 1
        if cnt[0] == cnt[1]: # u가 균형잡힌 문자열, v는 나머지
            return p[:i+1],p[i+1:]
        
def check(p): # p가 올바른 문자열인지 확인한다
    stack = []
    for char in p:
        if char == '(':
            stack.append(char)
        else: # ')'
            if not stack: # 비어있으면
                return False
            stack.pop()
    return True

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if not p:
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u,v = divide(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 
    if check(u):
        return u + solution(v) # 3-1. 문자열 v에 대해 1단계부터 다시 수행하고 결과를 u에 이어 붙인 후 반환합니다. 
    
    else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
        answer = '(' + solution(v) + ')'  # 4-1,2,3.
        for char in u[1:-1]:  # 4-4. u의 첫 번째와 마지막 문자를 제거하고
            if char == '(' : # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
                answer += ')'
            else: answer += '('
        return answer
    
        