from itertools import combinations, product

def solution(word):
    answer = 0
    words = []
    for i in range(5):
        words.append('A')
        words.append('E')
        words.append('I')
        words.append('O')
        words.append('U')
    
    dic = []
    for i in range(1,6):
        dic.extend(combinations(words,i))
    dic = list(set(dic))
    for i in range(len(dic)):
        dic[i] = "".join(dic[i])
    
    dic.sort()

    return dic.index(word)+1

# Product 란? 중복순열 
# 여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 수
# repeat = 뽑고자 하는 데이터의 수

def solution2(word):
    dic = []
    for i in range(1, 6):
        dic += list(map(''.join, product('AEIOU', repeat = i)))
    print(dic)
    dic.sort()
    return dic.index(word) + 1

print(solution2("AAAAE"))