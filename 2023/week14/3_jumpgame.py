class Solution:
    # Runtime 59.76% (480ms) Memory 7.25% (17.8MB)
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0] # 현재 max jump 값 

        for i in range(1, len(nums)):
            if curr == 0:
                return False
            curr -= 1 # 한칸씩 이동
            curr = max(curr, nums[i]) 
        return True   