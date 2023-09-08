class Solution:
    # Runtime 8.14% (7226ms) Memory 39.53% (18.5MB)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1 # 양쪽 끝과 끝부터 시작 
            while l<r:
                s = nums[l] + nums[i] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    b = [nums[l],nums[i],nums[r]]
                    if b not in answer:
                        answer.append(b)
                    l += 1
        return answer

    # Runtime 96.76% (898 ms) Memory 15.51% (18.8MB)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()

        # 양수, 음수, 0으로 나눠 담음
        neg, pos, zero = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)

        # 집합으로 중복제거
        neg_set, pos_set = set(neg), set(pos)

        # 0이 있으면 부호만 다른 수 있는지 확인해서 담음
        if zero:
            for num in pos_set:
                if -1*num in neg_set:
                    answer.add((-1*num, 0, num))

        # 0 세개 이상이면 담음
        if len(zero) >= 3:
            answer.add((0,0,0))

        # 음수의 모든 pair 보면서, 0을 만들 수 있는 양수 값 있는지 확인
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = -1*(neg[i]+neg[j])
                if target in pos_set:
                    answer.add(tuple(sorted([neg[i],neg[j], target])))
        
        # 양수의 모든 pair 보면서, 0을 만들 수 있는 음수 값 있는지 확인
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = -1*(pos[i]+pos[j])
                if target in neg_set:
                    answer.add(tuple(sorted([pos[i],pos[j],target])))

        return answer