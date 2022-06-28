import collections

def solution(clothes):
    dict = collections.defaultdict(list)
    for c in clothes:
        dict[c[1]].append(c[0])
    answer = 1
    for c in dict.values():
        answer *= (len(c)+1)
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	))

# 정석 풀이
def solution2(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
