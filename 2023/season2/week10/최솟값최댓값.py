# 단순 배열 (sum(nums[b-1:c])) -> 시간 초과  O(n)
# 세그먼트 트리 !  O(logN)
# 부모 노드의 데이터의 범위를 반씩 나누어 그 구간의 합들을 저장한다. 


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

op = []
for _ in range(m):
    op.append(list(map(int, input().split())))

# seg_tree[1] : 모든 노드의 합
# seg_tree[2] : 0 ~ (n//2)번 노드의 합
# seg_tree[3] : (n//2+1) ~ n번 노드의 합
seg_tree= [0 for _ in range(4*n)] # 데이터의 크기*4만큼 노드 할당

# 세그먼트 트리 만들기 : seg_tree[x] 값 구하기
def build_tree(x, left, right):
    if left == right:
        seg_tree[x] = (nums[left], nums[left])
        return seg_tree[x]

    mid = (left + right) // 2
    left_value = build_tree(2*x, left, mid) # 왼쪽 자식
    right_value = build_tree(2*x+1, mid+1, right) # 오른쪽 자식
    seg_tree[x] = (min(left_value[0], right_value[0]), max(left_value[1], right_value[1])) # 부모 노드는 양쪽 자식노드에서 min, max 선택 
    return seg_tree[x]

build_tree(1, 0, n-1)

# 세그먼트 트리에서 구간합 찾기
def find_tree(a, b, x, left, right): # 현재 노드x, 트리의 구간 left~right
    # 찾는 구간이 현재 트리 구간을 벗어나면
    if b < left or right < a: 
        return (10**9+1, 0) # 최대 min 값, 최소 max 값 반환
    
    # 찾는 구간 안에 현재 트리 구간 전체가 포함되면
    if a <= left and right <= b:
        return seg_tree[x]

    # 두 구간이 겹치는 경우 
    mid = (left + right) // 2
    left_value = find_tree(a, b, x*2, left, mid)
    right_value = find_tree(a, b, x*2+1, mid+1, right)
    return (min(left_value[0], right_value[0]), max(left_value[1], right_value[1]))

for a,b in op:
        s = find_tree(a-1, b-1, 1, 0, n-1)
        print(s[0], s[1])