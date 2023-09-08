class Solution:
    # Runtime 28.64% (151 ms) Memory 9.79% (19.2MB)
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k,v in cnt.items():
            if v == 1:
                return k

# 정석풀이 XOR Problem (167ms)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res

# 신박한 풀이 try except (15.7 MB)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            try:
                number = nums.pop()
                nums.remove(number)
            except:
                return number