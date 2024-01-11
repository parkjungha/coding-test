
N, K = map(int, input().split())
devices = list(map(int, input().split()))

multitap = [] # 현재 멀티탭 상태
ans = 0 

for i in range(K): 
    if devices[i] in multitap: # 현재 사용할 기기가 멀티탭에 꽂혀있다면
        continue

    if len(multitap) < N: # 현재 멀티탭에 빈 칸이 있다면
        multitap.append(devices[i]) # 현재 기기 플러그 꽂기
        continue
    
    removed = 0 # 뽑을 기기 번호 
    removedIdx = 0 # 뽑을 기기 인덱스

    # 현재 멀티탭에서 플러그를 빼고 꽂아야할 때, 최적의 선택
    for device in multitap: # 현재 멀티탭에 꽂혀있는 기기 중에서
        if device not in devices[i:]: # 나중에 사용될 기기 목록에 없으면
            removed = device
            break
        
        # 가장 나중에 사용될 기기 찾아서 뽑기
        elif devices[i:].index(device) > removedIdx:
            removedIdx = devices[i:].index(device)
            removed = device
    
    # 플러그 교체
    multitap[multitap.index(removed)] = devices[i]
    ans += 1

print(ans)

