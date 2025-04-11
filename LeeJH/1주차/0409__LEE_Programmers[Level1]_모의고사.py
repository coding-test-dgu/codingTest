def solution(answers):
    score = [0 for i in range(3)]
    # 3사람의 찍는 방식
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    answer =[]
    # answers의 크기만큼 반복
    for i in range (len(answers)):
        # answers의 0번부터 n번까지 각각 비교하면서 맞춘 개수를 체크
        ans = answers[i]
        if(ans == person1[i%5]):
            score[0] += 1
        if(ans == person2[i%8]):
            score[1] += 1
        if(ans == person3[i%10]):
            score[2] += 1
    
    for i in range(len(score)):
        # score가 최대인 사람의 인덱스(i+1)를 answer에 append
        if (score[i] == max(score)):
            answer.append(i+1)
    return answer