'''
접근 방법
- 안쪽의 yellow 영역으로 가로와 세로를 나눠서 접근
어려운 상황
- 
교훈
- range의 끝점은 범위에 포함 안됨.
  끝점까지 돌려보고 싶으면, 끝점+1을 해줘야함.
  이거 때문에 테케 하나가 안 됐던 것임.


'''



def solution(brown, yellow):
    answer = []
    
    for sero in range(1,yellow+1):
        if yellow % sero == 0:
            garo = yellow // sero
            print(garo, sero)
            if ((garo+2)*2 + (sero*2)) == brown:
                answer.append(garo+2)
                answer.append(sero+2)
                break

    return answer