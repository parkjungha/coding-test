def convert(num, base):
    temp = '0123456789ABCDEF'
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    test = ''

    for i in range(m*t): # 0부터 목표하는 숫자 (m*t)까지 다 n진수로 변환해서 문자열에 담아두기
        test += str(convert(i, n))

    while len(answer) < t:
        answer += test[p-1]  # 튜브 순서
        p += m # 사람 수만큼 인덱스를 증가

    return answer