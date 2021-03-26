# Qualification Round 2019 - 3 Dat Bae
# 2019.04.06 PBY
"""
input)
interactive
"""

# attempt 1&2&3 (Runtime Error)
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, B, F = map(int, input().split())
    # Broken 수만큼 0으로 바꿔서 보내면 되잖아...
    broken = list(range(B))
    comb = list(combinations(range(N), B))
    for attempt in range(F):
        testoutput = ''
        for i in range(N):
            if i in comb[attempt]:
                testoutput += '0'
            else:
                testoutput += '1'
        print(testoutput)
        testinput = input()
        if '0' not in testinput:
            # comb가 정답
            broken = list(comb[attempt])
            
    print(' '.join(list(map(str, broken))))
    verdict = int(input())
    if verdict == -1:
        break
