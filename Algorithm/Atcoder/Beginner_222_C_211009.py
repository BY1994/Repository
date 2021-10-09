"""
atcoder
#c
"""

def win(a, b):
    if a == 'G':
        if b == 'C':
            return 1
        elif b == 'P':
            return -1
    elif a == 'C':
        if b == 'G':
            return -1
        elif b == 'P':
            return 1
    elif a == 'P':
        if b == 'G':
            return 1
        elif b == 'C':
            return -1
    return 0

N, M = map(int, input().split())

games = []
scores = []
for i in range(2*N):
    scores.append([i, 0]) # init
    games.append(input())

# round
for i in range(M):
    scores.sort(key = lambda x: (-x[1], x[0]))
    for j in range(1, N+1):
        #print(f"{scores[2*j-1-1][0]} vs {scores[2*j-1][0]}")
        #print(f"{games[scores[2*j-1-1][0]][i]} vs {games[scores[2*j-1][0]][i]}")
        result = win(games[scores[2*j-1-1][0]][i], games[scores[2*j-1][0]][i])
        #print(result)
        if result == 1:
            scores[2*j-1-1][1] += 1
        elif result == -1:
            scores[2*j-1][1] += 1
    #print(scores)

scores.sort(key = lambda x: (-x[1], x[0]))

for i in range(2*N):
    print(scores[i][0]+1)
