class Solution:
    # Rumtime 98.99% (55ms) Memory 69.67% (16.3MB)
    # DFS로 가능한 조합 재귀적으로 만들기. 조합 안되는 경우에는 backtrack 

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        if sum(nums)%k != 0: return False

        nums.sort(reverse=True) # 내림차순 정렬
        avg = sum(nums) // k 
        visited = [0]*len(nums)

        # cur은 누적합 (0부터 avg까지)
        def dfs(cur, begin, k):
            if k == 0: # Base case: k개의 subset 다 만든 경우
                return True
            elif cur > avg: # 현재 subset이 성립 안되는 경우 
                return False 
            elif cur == avg: # 현재 subset이 만족하는 경우 -> 이제 k-1개 subset 더찾아야함
                return dfs(0, 0, k-1)
            
            # cur < avg 이면 남은 숫자 하나씩 보면서 만족하는 subset 찾기 -> DFS 재귀 + Backtracking
            for i in range(begin, len(nums)):
                if visited[i] or cur + nums[i] > avg:  # 이미 앞에서 사용한 숫자이거나, 누적합이 이미 avg 초과하면 X                    
                    continue
    
                visited[i] = 1
                if dfs(cur+nums[i], i+1, k): # 현재 숫자 가능하면 
                    return True 
                visited[i] = 0

                if cur == 0:
                    break ##### 여기 break 없으면 시간 초과 뜸

            return False

        return dfs(0,0,k)