# 규칙
# memo[n] = ['('와 ')' 사이에 memo[n-1]이 들어간 것들] 
# + [i+j=n 인 모든 i,j에 대해 memo[i] * memo[j]]


def solution(n):
    memo = [[],['()']]
    combi = [[]]
    for i in range(1, n+1): # 1 ~ n
        kinds = []
        for j in range(1, i+1):
            for k in range(1, i-j+1):
                if j + k == i:
                    kinds.append((j,k))
        combi.append(kinds)

# combi = [[], [], [(1, 1)], [(1, 2), (2, 1)], [(1, 3), (2, 2), (3, 1)], [(1, 4), (2, 3), (3, 2), (4, 1)]]  when n = 5

    for i in range(2, n+1):
        temp = []
        for l in memo[i-1]:
            temp.append('('+l+')') # '('와 ')' 사이에 memo[n-1]이 들어간 것
        for j, k in combi[i]:
            for t1 in memo[j]:
                for t2 in memo[k]:
                    temp.append(t1+t2)
        memo.append(list(set(temp)))

    return len(memo[n])

solution(5)