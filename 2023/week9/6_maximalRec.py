class Solution:
    # 앞 문제 그대로 활용 
    # Runtime 83.93% (254ms) Memory 14.72% (15.3MB)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        heights = [0]*m
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == "1"): # 1차원 어레이로 넣어줌
                    heights[j]+=1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea(heights)
            maxArea = max(area, maxArea)
        return maxArea
    
    # 앞문제 함수 
    def largestRectangleArea(self, bars):
        stack = []
        ans = 0

        for bar in bars+[0]: # 맨 마지막 bar 고려해주기 위해서 하나 추가 (ex: [2,4]->4) 
            pops = 0
            while stack and stack[-1][1] >= bar: # stack의 마지막 원소의 height과 현재 bar의 height 비교
                width, height = stack.pop()
                pops += width
                ans = max(ans, pops*height)

            stack.append([pops+1, bar])
        
        return ans