class Solution:
    # O(n^2) 단순 풀이 - TC 44에서 시간초과 하하
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings) # Each child must have at least one candy.
       
        condition = False

        while not condition: 
            condition = True
            for i in range(1, len(ratings)):
                if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                    candies[i] += 1
                    condition = False
                    
                elif ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                    candies[i-1] += 1
                    condition = False


        return sum(candies)

    # 앞에서부터 한번 검사, 뒤에서부터 한번 검사 O(n) 두번만
    # Run 36.14% (175ms) Mem 25.78% (19.3MB)
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1

        for i in range(len(ratings)-1, 0, -1): # 뒤에서부터
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1


        return sum(candies)