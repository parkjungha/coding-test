# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def solution(inputArray, k):
    curVal = maxVal = sum(inputArray[:k])
    for i in range(len(inputArray)-k):
        curVal += (inputArray[i+k] - input[i])
        maxVal = max(maxVal, curVal)
    return maxVal 