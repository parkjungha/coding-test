def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    for i,j in results:
        win[i].append(j) # win[i]: i가 이긴 애들
        lose[j].append(i) # lose[j]: j가 진 애들

    for i in range(1,n+1): # 모든 선수들에 대해서 정보 업데이트 할거
        for w in win[i]: # w는 i에게 진 선수 
            if lose[i]: 
                for l in lose[i]: # l은 i를 이긴 선수  
                    if l not in lose[w]: 
                        lose[w].append(l) # i에게 진 선수들은 i를 이긴 선수들에게 항상 진다
                    if w not in win[l]: # 이긴 선수들은 
                        win[l].append(w) # i를 이긴 선수들은 i에게 진 선수들을 항상 이긴다

    for w,l in zip(win,lose):
        if len(w)+len(l) == n-1:
            answer += 1
    return answer 

# 생각하는게 복잡 ㅠ 