import collections

def solution(genres, plays):
    answer = []
    genres_dict = collections.defaultdict(int) #장르별 총 재생횟수
    songs = collections.defaultdict(list)  #장르별 [재생횟수, 고유번호]

    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]
        songs[genres[i]].append([plays[i],i])
    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True) # 장르 정렬

    for genre in genres_dict:
        songs[genre[0]] = sorted(songs[genre[0]], key=lambda x:x[0], reverse=True)
        c = 0
        for s in songs[genre[0]]:
            if c==2:
                break
            answer.append(s[1])
            c += 1
            
    return answer
