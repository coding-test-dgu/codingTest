# 정렬
def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        # commands의 첫번째 행의 0번인덱스(i)와 1번인덱스(j)를 기준으로 array를 슬라이싱. 
        # 이때, i-1을 해야 i번째부터 슬라이싱한다.
        slice_array = array[commands[i][0]-1:(commands[i][1])]
        # 슬라이싱 된 array를 sort
        slice_array.sort()
        # commands의 k번째의 array의 index를 answer에 append(마찬가지로 k-1)
        answer.append(slice_array[commands[i][2]-1])

    return answer