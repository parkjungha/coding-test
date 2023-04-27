# Runtime 84.93% (30ms) Memory 63.24% (13.9MB)
class Solution:
    # '..' -> 이전 폴더로 -> stack 사용

    def simplifyPath(self, path: str) -> str:
        path = path.replace('//','/')
        pathList = path.split('/')
        stack = []
        
        for name in pathList:
            if name != '' and name != '..' and name != '.': # 일반적인 폴더명일 경우
                stack.append(name)
            elif name == '..' and stack: # 이전 폴더로 돌아가기
                stack.pop()

        return '/' + ('/'.join(stack)) # 반환 값 포맷팅