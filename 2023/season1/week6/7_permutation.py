class Solution:
    # permutation Runtime 18.67% (1791ms) Memory 8.82% (57.2 MB)
    def getPermutation(self, n: int, k: int) -> str:
        return [''.join(map(str, s)) for s in list(permutations(range(1,n+1)))][k-1] # 시간초과 
        
        return ''.join(map(str, list(permutations(range(1,n+1)))[k-1])) # 이건 통과됨 

    # 정석 .. Runtime 46ms 
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)] # list of numbers from 1 to n
        factorial = [1] * n # initialize factorial with n factorial of 1
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i # calculate the factorials
        
        k -= 1 # decrement k by 1, since k is 1-indexed
        result = []
        for i in range(n-1, -1, -1):
            index = k // factorial[i] # calculate the index of the number to be picked
            result.append(str(nums[index])) # add the number to result
            nums.pop(index) # remove the number from the list
            k = k % factorial[i] # update k
        
        return ''.join(result) # join the result list into a single string and return
