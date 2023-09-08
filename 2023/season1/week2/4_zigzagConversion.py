class Solution:
    # Runtime 27.87% Memory 27.10%
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: # 1이면 그냥 그대로
            return s

        ans = [[] for _ in range(numRows)]

        curr = 0
        dir = 1 # 처음엔 증가방향
        while s:
            if curr == len(ans): #  끝까지 도달
                curr -= 2
                dir = 0 # 감소 방향으로 전환
            if curr == -1: # 맨앞까지 도달
                curr += 2
                dir = 1 # 증가 방향으로 전환

            ans[curr].append(s[0])
            s = s[1:]

            if dir : curr += 1
            else: curr -= 1

        res = ""
        for el in ans:
            res += "".join(el)
        
        return res

    # Runtime 93.48% Memory 45.83%
    def convert2(self, s: str, numRows: int) -> str:
        pattern = list(range(numRows)) + list(range(numRows-2, 0, -1))
        times = math.ceil(len(s)/len(pattern))
        pattern *= times
        # [0 1 2 3 2 1 0 1 2 3 2 1 ... ]

        res = ["" for _ in range(numRows)]

        for idx, char in zip(pattern, s):
            res[idx] += char
        
        return "".join(res)
