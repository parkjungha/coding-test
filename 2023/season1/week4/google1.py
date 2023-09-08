
def problem1(moveInfo):
    cntA, cntC, cntQ, ans = 0,0,0,0

    for c in moveInfo.split():
        if c == 'A': 
            cntA += 1
        if c == 'C': 
            cntC += 1
        else: 
            cntQ += 1
        
        ans = max(ans, abs(cntA-cntC)) + cntQ

    return ans

def problem2(n, costA, costB):
    if n == 1: 
        return costA[0]
    
    minServerCost = [0 for _ in range(n)] # Dynamic Programming Array
    isAdjacent = [False for _ in range(n)]
    singleCost = 0
    adjacentCost = 0

    minServerCost[0] = costA[0] # 초기화
    if costA[0] + costA[1] > costB[0] + costB[1]:
        minServerCost[1] = costA[0] + costA[1]
        isAdjacent[1] = False
    else:
        minServerCost[1] = costB[0] + costB[1]
        isAdjacent[0] = True
        isAdjacent[1] = True
    
    for i in range(2, n):
        singleCost = minServerCost[i-1] + costA[i]
        if isAdjacent[i-1]: # True
            adjacentCost = minServerCost[i-1] + costB[i]
        else: # False
            adjacentCost = minServerCost[i-1] - costA[i-1] + costB[i-1] + costB[i]

        if singleCost > adjacentCost:
            minServerCost[i] = singleCost
            isAdjacent[i] = False
        else:
            minServerCost[i] = adjacentCost
            isAdjacent[i] = True
        
    return minServerCost[n-1]
