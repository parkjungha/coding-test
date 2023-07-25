class Solution:
    # Memory Limit Exceeded 29 / 30 testcases
    def isSelfCrossing(self, distance: List[int]) -> bool:
        currX, currY = 0,0
        track = {(currX,currY)}

        dx = [0,-1,0,1]
        dy = [1,0,-1,0]

        for i in range(len(distance)):
            for n in range(distance[i]):
                currX += dx[i%4]
                currY += dy[i%4]
                
                if (currX,currY) in track:
                    return True
                else:
                    track.add((currX,currY))
        
        return False

class Solution:
    # Memory optimized solutions
    
    def isSelfCrossing(self, distance: List[int]) -> bool:
        if len(distance) < 4:
            return False

        for i in range(3, len(distance)): # 어차피 북-서-남 에서는 만날 일 없으니까, 동 방향부터 봄
            # Three cases

            # 1. current distance >= second to last distance AND previous distance <= third to last distance
            # len(🠖) >= len(🠔) AND len(🠗) <= len(🠕)
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # 2. current distance + fourth to last distance >= second to last distance
            # i=4면 다시 북 방향
            # len(🠖) == len(🠔) and first len(🠕) + second len(🠕) >= len(🠗)
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            # 3. i=5면 서 방향
            # ... 
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] <= distance[i-3] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True
        return False 