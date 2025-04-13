function solution(array, commands) {
    var answer = [];
    for (i = 0; i < commands.length; i++) {
        slice_array = array.slice(commands[i][0] - 1, commands[i][1]);
        // 내림차순 (그냥 sort()함수는 문자열 크기 순서대로 정렬)
        slice_array.sort((a, b) => a - b);
        answer.push(slice_array[commands[i][2] - 1]);
    }
    return answer;
}
