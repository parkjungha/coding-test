def solution(citations):
    citations.sort(reverse=True) # 많이 인용된 순(내림차순)으로 정렬
    for idx, citation_num in enumerate(citations):
        if idx >= citation_num: # 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자
            return idx
    return len(citations)
