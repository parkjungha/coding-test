from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 모든 조합
    combi = []
    for i in range(1, col+1): # 1개부터 속성 개수까지
        combi.extend(combinations(range(col), i)) # 인덱스 조합으로 뽑음
    print(combi)


    # 유일성 체크 
    unique = []
    for c in combi:
        tmp = [tuple([item[i] for i in c]) for item in relation]
     #   print(tmp)
        if len(set(tmp)) == row:
            unique.append(c)
    
    # 최소성 체크
    answer = set(unique) # 사전 순서 정렬
    for i in range(len(unique)):
        for j in range(i+1, len(unique)): # 교집합 
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))