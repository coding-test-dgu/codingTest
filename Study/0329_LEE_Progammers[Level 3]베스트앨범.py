from collections import defaultdict

# 두개 dict만들어서, 첫번째 dict(dict_genre)는 key : 장르, value : 재생수, idx
# 두번째 dict(dict_total)는 key : 장르 , value = 총 재생수
# 다 넣어놓고, dict_total을 정렬해서 많이 재생된 장르 뽑고, 해당 장르로 dict_genre 반복돌면서 최대 두개로 뽑으면 될거같긴함
# 근데 일단 dict에 파라미터 넣는것부터 개헷갈리는중
def solution(genres, plays):
    dict_genre = defaultdict(list)
    dict_total = defaultdict(list)
    gen_dict = []
    N = len(genres)
    
    for i, (g,p) in enumerate(zip(genres, plays)):
        dict_genre[g].append((p,i))
    
    for g, p in dict_genre.items():
        total = 0
        for p in dict_genre[g]:
            total += p[0]
        dict_total[g] = total
   
    # 장르별 총 재생 수 기준으로 내림차순 정렬
    sorted_genres = sorted(dict_total.items(), key=lambda x: -x[1])

    answer = []
    for genre, _ in sorted_genres:
        # 각 장르별 노래를 재생 수 기준 내림차순, 고유번호 오름차순 정렬
        songs = sorted(dict_genre[genre], key=lambda x: (-x[0], x[1]))

        # 최대 2개까지 골라서 answer에 추가
        for song in songs[:2]:
            answer.append(song[1])  # 고유번호만 추가

    return answer