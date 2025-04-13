// function solution(numbers, target) {
//     let answer = 0;
//     let queue = [];
//     queue.push([0, 0]); // [total, idx]

//     while (queue.length > 0) {
//         const [total, idx] = queue.shift();

//         if (idx == numbers.length) {
//             if (total == target) {
//                 answer += 1;
//             }
//         } else {
//             queue.push([total + numbers[idx], idx + 1]);
//             queue.push([total - numbers[idx], idx + 1]);
//         }
//     }

//     return answer;
// }
// js로 bfs풀이방법 쓰면 shift()함수때문에 테케에서 시간초과 발생..=> DFS로 변경!
// JavaScript의 배열은 shift()시 요소들을 모두 한 칸씩 당겨야 함.그래서 큐가 클수록 성능이 급격하게 저하 O(N)

function solution(numbers, target) {
    let answer = 0;
    // 재귀함수로
    function dfs(idx, total) {
        if (idx === numbers.length) {
            if (total === target) {
                answer += 1;
            }
            return;
        }

        dfs(idx + 1, total + numbers[idx]);
        dfs(idx + 1, total - numbers[idx]);
    }

    dfs(0, 0);
    return answer;
}
