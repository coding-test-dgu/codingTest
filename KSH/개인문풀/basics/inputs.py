import sys

# data = sys.stdin.read()
# data = sys.stdin.read().rstrip()

# data = sys.stdin.readline()
# data = sys.stdin.readline().rstrip()

# data = sys.stdin.readlines()
# data = sys.stdin.readlines().rstrip() # AttributeError: 'list' object has no attribute 'rstrip'

# data = [line.split() for line in sys.stdin.readlines()]
# 결과 : ['1 0', '0 4', '3 3 7', '2 3 4 2']
# data = [line.split() for line in sys.stdin.readlines()]
# 결과 : [['1', '0'], ['0', '4'], ['3', '3', '7'], ['2', '3', '4', '2']]
data = [list(map(int, line.split())) for line in sys.stdin.readlines()]
# 결과 : [[1, 0], [0, 4], [3, 3, 7], [2, 3, 4, 2]]


print(data)


'''
입력 데이터

hi there
i love python
python can do anything.

1 0
0 4
3 3 7
2 3 4 2
'''