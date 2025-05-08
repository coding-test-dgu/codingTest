N = int(input())
students = list(map(int, input().split()))

stack = []

now_turn = 1

# Step1: 스택에 들어갈 사람 필터링
for student in students:

    # 지금 차례 아닌 사람은 stack에 삽입
    if student == now_turn:
        now_turn += 1
    # 지금 차례인 사람일 경우, 통과시키고 -> 다음 turn으로
    else:
        stack.append(student)

    # 매 순간 마다 stack에 들어간 top student가 바로 나올 수 있는지 없는지 체크해야함
    '''
    5
    2 1 5 3 4
    의 경우 2가 1이 통과되고 바로 2가 stack에서 나와야함
    '''
    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn += 1

if stack:
    print("Sad")
else:
    print("Nice")



