
def solution(user_id, banned_id):
    answer = []
    res = [[]] # 각 요소가 하나의 경우의 수를 나타냄
 
    for ban in banned_id: # banned_id 별로 가능한 user_id 리스트로 저장 
        li = []
        for user in user_id:
            if len(ban) != len(user):
                continue # 길이가 다르면 볼 필요 없으니까 다음으로 
            else:
                check = True
                for i in range(len(ban)): # 한글자씩 검사
                    if ban[i] == user[i] or ban[i] == '*':
                        continue 
                    elif ban[i] != user[i]:
                        check = False
                        break

                if check:
                    for c in res:
                        if user not in c:
                            li.append(c+[user])
        print(li)              
        res = li

    print(res)
    for s in res:
        if set(s) not in answer:
            answer.append(set(s)) # 중복이 없어야함

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	,["fr*d*", "*rodo", "******", "******"]	))