class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        profit = 0

        for price in prices:
            if price < minVal: # 최소 가격 stock 갱신하기
                minVal = price 
            profit = max(profit, price - minVal)
        
        return profit