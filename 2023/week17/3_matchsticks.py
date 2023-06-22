class Solution:
    # 앞문제랑 비슷. DFS로 가능한 path 계속 하나씩 추가하면서 재귀적으로 탐색 -> 안되는 경우 backtrack
    # Runtime 28.12% (7362 ms) Memory 74.89% (16.3MB)
    
    # break 넣었을 때::: Runtime 85.42% (383 ms) Memory 32.41% (16.4MB)
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target = total // 4
        if total % 4 != 0 or max(matchsticks) > target: # 사각형을 만들 수 없는 경우
            return False
        
        matchsticks.sort(reverse=True) # 내림차순 정렬

        def dfs(i, sides): # i: 현재 matchstick의 인덱스 / sides: 각 네 변의 길이를 담은 array
            if i == len(matchsticks) and all(side == target for side in sides):
                return True

            for j in range(4): # 네 변에 대해서 하나씩 확인
                if sides[j] + matchsticks[i] <= target: # 현재 matchstick을 현재 변에 넣는게 가능한 경우
                    sides[j] += matchsticks[i] # 넣어봄
                    if dfs(i+1, sides): # idx +1 해서 재귀 
                        return True
                    sides[j] -= matchsticks[i] # 다시 복원

                    if sides[j] == 0: # sides[j] 변에 현재 matchsticks을 처음 넣은 경우인데 이 변에서 실패한 경우는 나머지 변도 마찬가지기 때문에 바로 빠져나옴
                        break

            return False
        
        return dfs(0, [0,0,0,0])