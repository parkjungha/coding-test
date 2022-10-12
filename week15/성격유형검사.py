from collections import defaultdict
def solution(survey, choices):
    answer = ''
    scores = defaultdict(int)
    for i in range(len(survey)):
        choice = choices[i]
        if choice == 1:
            scores[survey[i][0]] += 3
        if choice == 2:
            scores[survey[i][0]] += 2
        if choice == 3:
            scores[survey[i][0]] += 1     
        if choice == 5:
            scores[survey[i][1]] += 1   
        if choice == 6:
            scores[survey[i][1]] += 2
        if choice == 7:
            scores[survey[i][1]] += 3   

    if scores["R"] >= scores["T"]:
        answer += "R"
    else: answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else: answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else: answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else: answer += "N"
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))