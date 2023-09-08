# 완전 탐색 : 시간초과 (36 / 49)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, i+indexDiff+1): # j는 i부터 index Diff까지만 보기
                if j >= len(nums):
                    continue 

                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True
        
        return False

class Solution:
    '''
    버킷 정렬(Bucket sort) 알고리즘: 평균 실행시간은 O(n) 
    범위 내에서 키값이 확률적으로 균등하게 분포된다고 가정할 수 있을 때 사용!!

    1. 데이터 n개가 주어졌을 때 데이터의 범위를 n개로 나누고 이에 해당하는 n개의 버킷을 만든다.
    2. 각각의 데이터를 해당하는 버킷에 집어 넣는다. (C 등에서는 연결리스트를 사용하며 새로운 데이터는 연결리스트의 head에 insert한다)
    3. 버킷별로 정렬한다.
    4. 전체적으로 합친다.
    '''
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {} # 길이가 valueDiff+1 인 Dictionary Bucket
        for idx, num in enumerate(nums):
            bucket = num // (valueDiff + 1) # bucket index

            # current bucket
            if bucket in buckets:
                return True
            
            # left adjacent bucket
            if bucket-1 in buckets and abs(num - buckets[bucket-1]) <= valueDiff:
                return True
            
            # right adjacent bucket
            if bucket+1 in buckets and abs(num - buckets[bucket+1]) <= valueDiff:
                return True

            # 아직 쌍이 없는 경우 bucket에 추가 
            buckets[bucket] = num

            if idx >= indexDiff: # bucket에서 삭제
                del buckets[nums[idx - indexDiff] // (valueDiff + 1)]

        return False

### Bucket sort Implemetation ###
def bucket_sort(seq):
    # Make buckets
    buckets = [[] for _ in range(len(seq))] # 데이터의 길이와 동일한 길이의 bucket 생성
    # Assign values
    for value in seq:
        bucket_index = value * len(seq) // (max(seq)+1) # 데이터의 범위를 n개로 나누고 bucket idx 생성
        buckets[bucket_index].append(value) # 해당하는 버킷에 넣는다
    
    # Sort by each bucket & Merge
    sorted_list = []
    for bucket in buckets:
        sorted_list.append(sort(bucket))
    return sorted_list

# https://ratsgo.github.io/data%20structure&algorithm/2017/10/18/bucketsort/ 참고