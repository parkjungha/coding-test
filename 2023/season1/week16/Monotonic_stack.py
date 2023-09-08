
def increasingStack(arr):
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] > arr[i]: 
            stack.pop()
        stack.append(arr[i])

    