class Solution:
  # 제일 쌀 때 사서 제일 비쌀 때 판다
  # 거래 한번하는 경우 최대 수익, 거래 두번하는 경우 최대 수익 나눠서 
  # Runtime 94.33% (1058ms) Memory 35.83% (30.1MB)
  
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
     
    buy1, buy2 = float('inf'), float('inf') # 최소 가격 저장
    sell1, sell2 = 0, 0 # 얻을 수 있는 최대 수익 저장

    for price in prices:
        # 거래 한번만 하는 경우
        buy1 = min(buy1, price) # 현재 가격이 최저점일 경우 갱신
        sell1 = max(sell1, price - buy1) # 현재 최대 수익과 (현재 가격 - 최저점) 비교  

        # 거래 두번하는 경우도 고려함. 한번만 했을때와 비교해서 더 큰 수익 
        buy2 = min(buy2, price - sell1) # 현재 가격에서 첫번째 거래까지 고려해서 최저 가격 갱신 
        sell2 = max(sell2, price - buy2)

    return sell2