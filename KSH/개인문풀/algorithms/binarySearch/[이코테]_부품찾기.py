import sys

n, store, m, request = [list(map(int, line.split())) for line in sys.stdin.readlines()]

def b_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

store.sort()

for i in range(m[0]):
    if b_search(store, request[i], 0, n[0]):
        print("yes")
    else:
        print("no")