class Solution(object):
    # Brute force: 모든 조합에 대해서 다 확인 O(n^2)
    def maxArea(self, height):
        max_container = 0
        for x1 in range(len(height)):
            for x2 in range(x1+1, len(height)):
                min_height = min(height[x1], height[x2])
                width = x2 - x1
                container = min_height * width
                max_container = max(max_container, container)

        return max_container

    # Two pointer: O(n)
    def maxArea2(self, height):
        x1 = 0
        x2 = len(height) -1
        max_container = 0
        while x1 < x2:
            min_height = min(height[x1], height[x2])
            width = x2 - x1
            container = min_height * width
            max_container = max(max_container, container)
            if height[x1] <= height[x2]: # 더 작은거 한칸씩 옮김 
                x1 += 1
            else:
                x2 -= 1
        return max_container