def solution(array, commands):
    answer = [] # 정답 배열
    
    for i,j,k in commands: # commands에 있는 원소에 1대1 대응
        custom_arr = sorted(array[i-1:j]) # array 정렬
        answer.append(custom_arr[k-1]) # array의 k 번째 수 정답 배열 삽입

    return answer