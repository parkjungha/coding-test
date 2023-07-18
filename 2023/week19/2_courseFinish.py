class Solution:
    # BFS -> Queue 사용
    # Runtime 83.69% (110ms) Memory 90.41% (17.7MB)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 연결된 노드간 cycle이 있는지 판별 
        graph = [[] for i in range(numCourses)] # adjacency matrix
        for i,j in prerequisites:
            graph[i].append(j) # directed edge. i를 듣고 나서 j를 들어야한다. i->j

        degree = [0]*numCourses # 각 노드로 들어오는 edge의 개수 (indegree) 저장
        complete = [] # 완료한 수업들 저장
        q = deque() # 현재 들을 수 있는 수업 순서대로 탐색 

        for i in range(numCourses):
            for j in graph[i]: # i와 연결된 모든 이웃 노드 j에 대해서
                degree[j] += 1 # j 전에 들어야하는 수업의 개수 count

        for i in range(numCourses):
            if degree[i] == 0: # i 전에 들어야하는 수업이 없다면
                q.append(i) # queue에 넣어서 이들부터 탐색 시작

        while q:
            course = q.popleft() 
            complete.append(course) # 해당 수업 들음
            for i in graph[course]: # 해당 수업을 듣고 난 이후에 들을 수 있는 수업들
                if degree[i] != 0: # prerequisites 수업 cnt 하나 빼줌
                    degree[i] -= 1 
                if degree[i] == 0: # 이전에 들어야하는 수업이 없다면
                    q.append(i) # queue에 넣기
        
        # Queue가 비었는데
        if len(complete) != numCourses: # 완료한 수업이랑 전체 수업 개수가 다르면
            return False

        return True
