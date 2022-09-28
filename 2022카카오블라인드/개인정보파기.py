def solution(today, terms, privacies):
    answer = []
    info = {}
    tyear, tmon, tday = map(int,today.split('.')) # 오늘

    for t in terms:
        info[t.split()[0]] = int(t.split()[1])

    num = 0
    for p in privacies:
        date, typ = p.split()
        year, mon, day = map(int,date.split('.'))
        num += 1

        mon += info[typ]
        if mon > 12:
            mon -= 12
            year += 1
        
        # 오늘 날짜랑 비교
        if year < tyear: # 연도가 이미 지났으면
            answer.append(num)
            continue
        elif year > tyear: continue

        # 연도가 같을 때
        if mon < tmon: # 달이 지났으면
            answer.append(num)
            continue
        elif mon > tmon: continue

        # 달도 같을 때
        if day <= tday:
            answer.append(num)
            continue
        elif day > tday: continue

    
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))