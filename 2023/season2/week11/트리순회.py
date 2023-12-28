import sys
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int,input().split())) # 왼-루트-오
postorder = list(map(int,input().split())) # 왼-오-루트

# preorder (루트-왼-오) 값 출력!!

inorder_idx = [0]*(n+1) # 중위순회 트리의 인덱스
for i in range(n):
    inorder_idx[inorder[i]] = i

def preorder(in_left, in_right, post_left, post_right):
    # 재귀 종료 조건
    if (in_left > in_right) or (post_left > post_right):
        return
    
    # postorder의 맨 마지막 노드 -> 현재 서브트리의 루트 노드
    root = postorder[post_right]
    print(root, end = ' ') # 루트 먼저 출력

    # 루트 노드를 기준으로, inorder의 왼쪽 오른쪽 서브트리 인덱스 나눔
    in_root = inorder_idx[root] # inorder에서 루트의 인덱스
    left = in_root - in_left # 왼쪽 서브트리 개수
    right = in_right - in_root # 오른쪽 서브트리 개수

    # 왼쪽 오른쪽 서브트리 각각 탐색- 재귀
    preorder(in_left, in_root - 1, post_left, post_left + left - 1)
    preorder(in_root + 1, in_right, post_right - right, post_right - 1)


preorder(0, n-1, 0, n-1)