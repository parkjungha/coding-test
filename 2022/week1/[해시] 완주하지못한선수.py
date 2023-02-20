def solution(participant, completion):
    # 효율성 X
    for c in completion:
        participant.remove(c)
        
    return participant[0]

    # 효율성 O 
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] == completion[i]: 
            continue
        else:
            return participant[i]