'''
배운점
- 자꾸 변수를 넣을 때, 아무 생각 없이 넣음.
    내가 어떤 케이스를 다루고 있는지, 내가 어떤 작업을 하고 있는지
    항상 인지하면서 코드를 짜야할 것 같다.
- 처음에는 팀을 나누는 케이스에 따라 코드를 짜려고 했다가,
    Sij와 Sji의 합 리스트를 만들어서
    이를 팀을 나누는 식으로 진행해보려고 했다가,
    머리 꼬여서 다시 처음 방식으로 진행함
    -> 결국 팀을 한번 나눠주는게 가장 빠른 것 같음

'''



import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
stat = [list(map(int, line.split())) for line in sys.stdin.readlines()]

people = [x for x in range(0,n)]

cases = list(combinations(people, n//2))
cases = cases[:len(cases)//2] # 어차피 중복되니니 - 이거 왜 처음에 10이라고 썼냐. 왜 임의 케이스를 넣냐고.

diffList = []

for case in cases:   # 가능한 팀의 조합 각 case에 대해
    teamA = case
    teamB = tuple(set(people)-set(case))
    teamA_case = list(combinations(teamA, 2))
    teamB_case = list(combinations(teamB, 2))

    teamA_sum = 0
    teamB_sum = 0

    for i,j in teamA_case:
        teamA_sum += stat[i][j]+stat[j][i]
    
    for i,j in teamB_case:
        teamB_sum += stat[i][j]+stat[j][i]
    
    diff = abs(teamA_sum-teamB_sum)
    diffList.append(diff)

print(min(diffList))