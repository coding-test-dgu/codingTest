def solution(answers):
    
    # 각 학생 정답 배열열
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    q = 0 # 문제 번호 - 0번 부터 시작
    
    scr1, scr2, scr3 = 0, 0, 0 # 학생 1,2,3 점수 변수 선언
    
    for ans in answers: # 정답들을 하나씩 비교
        if ans == s1[q%len(s1)]: # 학생 1 정답이면
            scr1 += 1
        if ans == s2[q%len(s2)]: # 학생 2 정답이면
            scr2 += 1
        if ans == s3[q%len(s3)]: # 학생 3 정답이면
            scr3 += 1
        q += 1
    
    print(scr1, scr2, scr3) # 학생별 점수 디버깅
    
    # 학생 번호와 학생별 점수를 enmuerate 및 정렬렬
    scores = [scr1, scr2, scr3]
    scores = list(enumerate(scores))
    scores = sorted(scores, key=lambda x: -x[1])
    
    print(scores)
    
    if scores[0][1] == scores[2][1]:        # 만일 양끝 학생 점수가 같으면
        answer = [scores[0][0]+1, scores[1][0]+1, scores[2][0]+1]
    elif scores[0][1] == scores[1][1]:      # 만일 첫번째와 두번째 점수가 같으면
        answer = [scores[0][0]+1, scores[1][0]+1]
    else:                                   # 둘 다 아니면
        answer = [scores[0][0]+1]
        
    return answer