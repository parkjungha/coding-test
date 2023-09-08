class Solution:
    # TLE 60 / 67 
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumulatedSum = [0]
        for n in nums: # nums = [-2,5,-1]
            cumulatedSum.append(cumulatedSum[-1] + n) # 누적합 리스트 만들기 ex: [0, -2, 3, 2]
 
        record = defaultdict(int) 

        # cumulated[j] - cumulated[i] is in [lower, upper]를 만족하는 경우를 세야함
        ans = 0 # count 
        for csum in cumulatedSum: # 각 누적합 리스트 원소들
            for target in range(lower, upper+1):
                if csum - target in record:
                    ans += record[csum - target]
            record[csum] += 1

        # csum = 0 일때, record = {0: 1}, ans = 0
        # csum = -2 일때, record = {0: 1, -2: 1}, ans = 1 (target = -2일때 ans += 1)
        # csum = 3 일때, record = {0: 1, -2: 1, 3: 1}, ans = 1
        # csum = 2 일때, record = {0: 1, -2: 1, 3: 1, 2: 1}, ans = 3 (target = -2일때랑 -1일때 ans +=1)
        
        return ans

    ###########################################################################################
    # Bisect: 정렬된 배열에서 특정 원소 찾을때 O(logN)에 동작
    # bisect_left(a, x) : 정렬 유지하면서 리스트 a에 데이터 x 삽입할 가장 왼쪽 인덱스 찾기
    # bisect_right(a, x) : 정렬 유지하면서 리스트 a에 데이터 x 삽입할 가장 오른쪽 인덱스 찾기

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumulatedSum = [0]
        for n in nums: # nums = [-2,5,-1]
            cumulatedSum.append(cumulatedSum[-1] + n) # 누적합 리스트 만들기 ex: [0, -2, 3, 2]
        
        cumulatedSum.pop(0) # 맨 앞 0 제거
        new_acc = sorted(cumulatedSum) # 정렬

        ans = 0
        num = 0

        # takes O(n)        
        for i in range(0, len(nums)):
            # get how many subarrays are within the bound
            # inside the loop, takes O(logn)
            l = bisect_left(new_acc, lower)
            r = bisect_right(new_acc, upper)
            diff = r - l

            ans += diff
            lower += nums[num]
            upper += nums[num]
            popped = bisect_left(new_acc, cumulatedSum[num])
            new_acc.pop(popped)
            num += 1

        return ans