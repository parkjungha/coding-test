class Solution:
    # Runtime 5.6% (7426ms ..........) 
    def maxPoints(self, points: List[List[int]]) -> int:
        # 가능한 모든 두개의 점에 대해서 방정식 만들고 다른 점들 확인해서 max count 갱신
        maxCnt = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)): 
                cnt = 0
                x1, y1 = points[i]
                x2, y2 = points[j]
                if not x1 - x2: # x변화량(분모)가 0인 경우
                    for point in points:
                        if point[0] == x1:
                            cnt += 1
                    maxCnt = max(maxCnt, cnt)
                    continue 
                
                m = (y1 - y2)/(x1 - x2) # 기울기
                b = y1 - m*x1 # y절편
                for x,y in points: # 점 하나씩 대입해서 방정식 성립하는지 확인 -> overhead 큼
                    if y == round(m*x + b, 5): # 부동소수점 비교에서 오차 해결하려고 반올림
                        cnt += 1
             
                maxCnt = max(maxCnt, cnt)
        return maxCnt

class Solution:
    # Runtime 64.81% (93s)
    def maxPoints(self, points: List[List[int]]) -> int:
        maxCnt = 1
        for i in range(len(points)):
            m_map = {} # (기울기, y절편) : 개수 정보 저장 
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if not x1 - x2:
                    m,b = None, None
                else:
                    m = (y1 - y2)/(x1 - x2) # 기울기
                    b = y1 - m*x1 # y절편
                
                t = (m,b)
                if t in m_map: # 이미 있으면
                    m_map[t] += 1
                else: # initialize 
                    m_map[t] = 2
           
                maxCnt = max(maxCnt, m_map[t]) # 최대 점 개수 갱신
    
        return maxCnt

