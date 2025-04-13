def solution(answers):
    scores = [0, 0, 0]
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 각 학생의 idx번 문제를 한번에 확인하는 방식(한 사람 다 끝내고 다음 사람 X)
    for idx, answer in enumerate(answers):
        for student_idx, pattern in enumerate(patterns):
            if answer == pattern[idx % len(pattern)]:
                scores[student_idx] += 1

    max_score = max(scores)

    return [student_idx + 1 for student_idx, score in enumerate(scores) if score == max_score]

