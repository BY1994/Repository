"""
1)
comp = 1
compval = 1
이렇게 실수해서 점수 계산이 잘못되었다.
2)
if dance[r][c] == 0:
이 조건 안 넣어줘서 자기 점수가 0인 경우 항상 꼴지니까 무한 루프에 빠졌다.
"""

for testcase in range(1, int(input())+1):
    R, C = map(int, input().split())
    dance = []
    anssum = 0
    for r in range(R):
        dance.append(list(map(int, input().split())))

    # round 진행
    while True:
        deleted = []
        for r in range(R):
            print(anssum, sum(dance[r]))
            anssum += sum(dance[r])
            for c in range(C):
                comp = 0
                compval = 0
                if dance[r][c] == 0:
                    continue
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= r+dx < R and 0<= c+dy <C and dance[r+dx][c+dy] != 0:
                        comp += 1
                        compval += dance[r+dx][c+dy]
                if comp and ((compval // comp + (compval % comp)*0.1) > dance[r][c]):
                    deleted.append((r, c))
        # 다 돌고 나면 0으로
        if len(deleted) == 0:
            break
        for d in deleted:
            dance[d[0]][d[1]] = 0

    print("Case #%d: %d" %(testcase, anssum))
                

