def solution(answers):
    answer = [0,0,0]

    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == answer1[i%len(answer1)]:
            answer[0] += 1
        if answers[i] == answer2[i%len(answer2)]:
            answer[1] += 1
        if answers[i] == answer3[i%len(answer3)]:
            answer[2] += 1
    li = []
    max_val = max(answer)
    for idx, val in enumerate(answer):
        if max_val == val:
            li.append(idx+1)
            
    return sorted(li)

print(solution([1,2,3,4,5]))