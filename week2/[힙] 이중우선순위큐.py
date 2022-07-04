import heapq
def solution(operations):
    minheap = []
    for op in operations:
        if op.split()[0] == "I": # 삽입
            heapq.heappush(minheap,int(op.split()[1]))    
            
        elif minheap and op == "D 1": # 최댓값 삭제 -> heapq에서 지원하지 않는 연산이기 때문에 그냥 list 연산으로 처리 
            minheap.remove(max(minheap))
        elif minheap and op == "D -1": # 최솟값 삭제
            heapq.heappop(minheap)
        
    if not minheap:
        return [0,0]
    else:
        return [max(minheap),heapq.heappop(minheap)]