# 장르별 해시 테이블 - 재생횟수:고유번호, 장르별 재생횟수 해시 테이블
# 장르별 HT 정렬, 장르별 재생횟수 HT도 정렬
# 재생횟수 많은 장르부터 top2개 노래 출력

from collections import defaultdict

def solution(genres, plays):
    
    # 데이터 집어넣을 dict 초기화
    genres_plays = defaultdict(int) # 장르별 총 재생횟수 dict
    g = genres_plays                # g로 편하게 
    songs = defaultdict(list)       # 각 노래별로 key = 장르, value = [(재생횟수, 고유번호), (재생횟수, 고유번호) ...]
    
    
    for i in range(0,len(genres)):           # 노래 갯수만큼 반복
        g[genres[i]] += plays[i]             # 장르별 재생 횟수 더해줌
        # songs[plays[i]] = [i, genres[i]]
        songs[genres[i]] += [(plays[i], i)]  # 각 노래별로 key = 장르, value = [(재생횟수, 고유번호), (재생횟수, 고유번호) ...]
    
    # 정렬 위해 list로 type 변환
    g = list(g.items())       
    songs = list(songs.items())
    
    g.sort(key=lambda x:x[1], reverse=True) # 정렬 수행: 재생 횟수별로 정렬
    songs.sort() # 정렬 수행
    
    # 딕셔내리로 재 변환
    g = dict(g) 
    songs = dict(songs) 
    
    # 디버깅용
    print(g)
    print(songs)
    
    for k in songs.keys(): # 장르별 value를 정렬하기 위해
        songs[k] = sorted(songs[k], key=lambda x: (-x[0], x[1]))
    
    # 출력할 결과 리스트 result 선언
    result = []
    
    # result에 장르 순서에 따라 노래 고유 번호 삽입
    for k in g.keys():
        v = songs[k]
        if len(v) == 1: # 장르에 해당하는 노래가 1개일때
            result.append(v[0][1])
        else:           # 장르 해당하는 노래가 2개 이상일 때
            result.append(v[0][1])
            result.append(v[1][1])
            
    return result