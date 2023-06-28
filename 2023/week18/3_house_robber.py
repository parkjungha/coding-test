class Solution:
    # Return the maximum amount of money. 인접한 칸은 털수 없음. @첫번째칸-마지막칸도 인접한 칸으로 취급@
    # Runtime 60.38 Memory 40.45
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        # prev는 현재 값을 기준으로 두칸 앞의 누적 합
        # curr는 인접한 바로 앞 칸 누적 합
        def helper(nums):
            prev, curr = 0,0
            for n in nums:
                tmp = max(n+prev, curr)
                prev = curr
                curr = tmp
                 
            return curr

        return max(helper(nums[1:]), helper(nums[:-1]))