

def solution(number, k):
    answer = ''
    stack = []
    for i in number: # number에 앞에 있는 숫자부터 스택에 넣어서, push()되는 값보다 작은 값들이 있으면 pop()해주고 pop() 횟수가 삭제된 k만큼 수행하는 것
        while stack and stack[-1] < i and k>0:
            k -= 1
            stack.pop()
        stack.append(i)
    return "".join(stack[:len(stack)-k]) # 제거 횟수를 다 사용하지 않았을때 남은 횟수만큼 리스트 뒷부분을 잘라 줌

    