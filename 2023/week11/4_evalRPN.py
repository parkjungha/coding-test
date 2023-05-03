class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'

        for token in tokens:
            if token in operators: 
                el2 = stack.pop() 
                el1 = stack.pop()

                if token == '+':
                    stack.append(el1 + el2)
                elif token == '-':
                    stack.append(el1 - el2)
                elif token == '*':
                    stack.append(el1 * el2)
                else:
                    stack.append(int(el1 / el2))
            
            else: # 숫자이면
                stack.append(int(token)) # stack에 쌓

        return int(stack.pop())