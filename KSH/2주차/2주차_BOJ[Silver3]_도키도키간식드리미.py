'''
배운점
- 반복문은 항상 종료 조건 2가지가 있어야함.
    1. 조건이 만족했을 때 종료 조건
    2. 반복 진행중, 모종의 이유로 반복이 더이상 불가능할 때의 종료 조건
        - 얘는, 백트래킹이랑도 연결됨

'''


from collections import deque
import sys

info = [list(map(int, line.split())) for line in sys.stdin.readlines()]

n = info[0][0]
line = info[1]

q = deque(line)
stack = []

turn = 1
cando = 1

while True:

    if turn == n: # 이 부분 왜 생각 못했지? - 반복문 조건 종료를 명심해야함
        break

    if len(q)>0 and q[0] == turn:
        q.popleft()
        turn += 1
    elif len(stack)>0 and stack[-1] == turn:
        stack.pop()
        turn += 1
    else:
        if not q:
            cando = 0
            break
        moving_person = q.popleft()
        stack.append(moving_person)

if cando == 0:
    print("Sad")
else:
    print("Nice")