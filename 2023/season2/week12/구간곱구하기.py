# 단순 배열 (sum(nums[b-1:c])) -> 시간 초과  O(n)
# 세그먼트 트리 !  O(logN)
# 부모 노드의 데이터의 범위를 반씩 나누어 그 구간의 합들을 저장한다. 

import sys
input = sys.stdin.readline
MOD = 1000000007

n, m, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

op = []
for _ in range(m+k):
    op.append(list(map(int, input().split())))

# seg_tree[1] : 모든 노드의 합
# seg_tree[2] : 0 ~ (n//2)번 노드의 합
# seg_tree[3] : (n//2+1) ~ n번 노드의 합
seg_tree= [0 for _ in range(4*n)] # 데이터의 크기*4만큼 노드 할당

# 세그먼트 트리 만들기 : seg_tree[x] 값 구하기
def build_tree(x, left, right):
    if left == right:
        seg_tree[x] = nums[left]
        return seg_tree[x]

    mid = (left + right) // 2
    left_value = build_tree(2*x, left, mid) # 왼쪽 자식
    right_value = build_tree(2*x+1, mid+1, right) # 오른쪽 자식
    seg_tree[x] = (left_value * right_value) % MOD # 부모 노드는 양쪽 자식노드들의 합 
    return seg_tree[x]

build_tree(1, 0, n-1)

# 세그먼트 트리에서 구간합 찾기
def find_tree(b, c, x, left, right): # b~c 구간, 현재 노드x, 트리의 구간 left~right
    # 찾는 구간이 현재 트리 구간을 벗어나면
    if c < left or right < b: 
        return 1
    
    # 찾는 구간 안에 현재 트리 구간 전체가 포함되면
    if b <= left and right <= c:
        return seg_tree[x]

    # 두 구간이 겹치는 경우 
    mid = (left + right) // 2
    left_value = find_tree(b, c, x*2, left, mid)
    right_value = find_tree(b, c, x*2+1, mid+1, right)
    return (left_value * right_value) % MOD

# 세그먼트 트리 값 업데이트
def update_tree(x, left, right, idx, val): # idx번째 값을 val로 변경
    if left == right == idx:
        seg_tree[x] = val
        return

    # idx가 범위를 벗어난 경우 
    if idx < left or right < idx:
        return 

    mid = (left + right) // 2
    update_tree(x*2, left,mid, idx, val) # 왼쪽 자식 업데이트
    update_tree(x*2+1, mid+1, right, idx, val) # 오른쪽 자식 업데이트
    
    # 업데이트된 양쪽 자식 노드 값으로 현재 부모 노드 업데이트
    seg_tree[x] = (seg_tree[x*2] * seg_tree[x*2+1]) % MOD

for a,b,c in op:
    if a == 1: # b번째 수를 c로 바꾸기
        update_tree(1, 0, n-1, b-1, c)
    else: # b~c 구간 합 구하기
        s = find_tree(b-1, c-1, 1, 0, n-1)
        print(s)