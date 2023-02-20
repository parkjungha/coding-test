import math

def solution(m, musicinfos):
    answer = None
    # 치환
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")

        hour, min = map(int, start.split(":"))
        start = hour*60 + min

        hour, min = map(int, end.split(":"))
        end = hour*60 + min

        duration = end - start # 음악 재생 시간

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        code *= math.ceil(duration / len(code)) # 음 충분히 반복하고
        code = code[:duration] # 딱 duration 길이 만큼 잘라줌

        if m not in code:
            continue
        
        # m을 포함한다면
        # 여러곡일 때는 1. 재생시간 더 긴거 2. 시작이 더 빠른거 
        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
            answer = (duration, start, title)

    if answer: # None 이 아니면
        return answer[2] # 노래 제목 
    
    return "(None)" # None이면