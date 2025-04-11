function solution(answers) {
    var answer = [];
    var score = [0, 0, 0];
    var person1 = [1, 2, 3, 4, 5];
    var person2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    for (i = 0; i < answers.length; i++) {
        var ans = answers[i];
        if (ans == person1[i % 5]) {
            score[0] += 1;
        }
        if (ans == person2[i % 8]) {
            score[1] += 1;
        }
        if (ans == person3[i % 10]) {
            score[2] += 1;
        }
    }
    for (j = 0; j < score.length; j++) {
        // 배열에서 Spread Operation 사용
        if (score[j] == Math.max(...score)) {
            answer.push(j + 1);
        }
    }
    return answer;
}
