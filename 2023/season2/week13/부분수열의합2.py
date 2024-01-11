# 시간복잡도 신경 X 풀이

# 1. 모든 조합 구해서 조건에 따라 개수 세기
for i in range(len(nums)+1):
    for c in combinations(nums, i):
        if sum(c) == S:
            ans += 1

if S == 0: 
    ans -= 1  

print(ans)  

####################################################
# 시간 복잡도 해결을 위해 왼오른쪽 나눠서 해결 #    

from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

leftNum = nums[:N//2]
rightNum = nums[N//2:]

leftSum, rightSum = [], []

# 왼쪽 수열에 대해 부분수열의 합 모두 저장
for i in range(len(leftNum) + 1):
    for c in combinations(leftNum, i):
        leftSum.append(sum(c))

# 오른쪽 수열에 대해 부분수열의 합 모두 저장
for i in range(len(rightNum) + 1):
    for c in combinations(rightNum, i):
        rightSum.append(sum(c))

# 왼쪽은 오름차순 정렬, 오른쪽은 내림차순 정렬
leftSum.sort()
rightSum.sort(reverse=True)

ans = 0
leftIdx, rightIdx = 0, 0 # 왼쪽 오른쪽 수열의 포인터
while leftIdx < len(leftSum) and rightIdx < len(rightSum):
    lval, rval = leftSum[leftIdx], rightSum[rightIdx]
    tmpSum = lval + rval # 현재 왼오른쪽 포인터가 가르키는 값의 합

    if tmpSum == S: 
        tmpLidx, tmpRidx = leftIdx, rightIdx
        
        while tmpLidx < len(leftSum) and leftSum[tmpLidx] == lval:
            tmpLidx += 1
        while tmpRidx < len(rightSum) and rightSum[tmpRidx] == rval:
            tmpRidx += 1
        
        ans += (tmpLidx - leftIdx) * (tmpRidx - rightIdx)
        leftIdx, rightIdx = tmpLidx, tmpRidx

    elif tmpSum < S:
        leftIdx += 1
    else:
        rightIdx += 1
    
if S == 0:
    ans -= 1

print(ans)

# https://c4u-rdav.tistory.com/61