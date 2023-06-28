class Solution:
  # Runtime 68.68% Memory 58.11%
  def addOperators(self, num: str, target: int) -> List[str]:
    ans = [] 

    # 현재 index , 이전 연산자 기호, 연산한 값, 
    def dfs(start, prev, eval, path):
      if start == len(num):
        # 정답 찾은 경우
        if eval == target:
          ans.append(''.join(path))
        return

      for i in range(start, len(num)):
        if i > start and num[start] == '0':
          return
        s = num[start:i + 1]
        curr = int(s)

        # 첫번째 글자는 단순 + 처리
        if start == 0:
          path.append(s)
          dfs(i + 1, curr, curr, path)
          path.pop()

        # 나머지는 +, -, * 하나씩 해보면서 가능한 경우 찾기 
        else:
          for op in ['+', '-', '*']:
            path.append(op + s)

            if op == '+':
              dfs(i + 1, curr, eval + curr, path)

            elif op == '-':
              dfs(i + 1, -curr, eval - curr, path)

            else:
              dfs(i + 1, prev * curr, eval - prev + prev * curr, path)
            path.pop()

    dfs(0, 0, 0, [])
    return ans