# Stack 
def solution(inputString):
    stack = []
    for x in inputString:
        if x == ')':
            tmp = ''
            while stack[-1] != '(': # ( 나올때까지 char 더해줌 
                tmp += stack.pop()
            stack.pop() # ( POP
            for item in tmp:
                stack.append(item) # 뒤집어져서 추가됨
        else:
            stack.append(x)

    return ''.join(stack) 

# 재귀
def solution(inputString):
    for i in range(len(inputString)):
        if inputString[i] == '(':   
            start = i
            
        elif inputString[i] == ')':
            end = i
            return solution(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
            
    return inputString