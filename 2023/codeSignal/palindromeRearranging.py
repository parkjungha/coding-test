def palindromeRearranging(inputString):
    cnt = 0
    for s in set(inputString):
        if inputString.count(s)%2 != 0:
            cnt += 1
        
    return cnt <= 1
