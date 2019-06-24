"""
15653 구슬 탈출 4

input)
10 6
######
#....#
#.#..#
#..#R#
##.#.#
#....#
#.#.B#
#..#O#
#.#..#
######

답은 2인데, 고치기 전에는 -1이 나왔다.
https://boohyunsik.github.io/exit-marble-test-case/

2019.06.22 PBY 최초작성
"""

# 

# 틀렸습니다 => visited에 R만 넣었다가 B, R 상태 동시에 넣는 걸로 변경
# + 거기에 플러스 가는 모든 길을 다 visited에 넣어줘야 빠꾸가 안 일어남...
N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
visited = [] # R과 B의 상태를 모두 넣지 않으면 안 되는 듯
for row in range(N):
    temp = input()
    for col in range(M):
        if temp[col] == 'B':
            Bloca = [row, col]
        elif temp[col] == 'R':
            Rloca = [row, col]
        board[row][col] = temp[col]
        
visited.append((Bloca, Rloca))

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = [(Bloca, Rloca)]
lenq = 1

ans = -1
cnt = 0
while q:
    print(q)
    cnt += 1
    for l in range(lenq):
        Bloca, Rloca = q.pop(0)
        print("q뺐잖아")
        print(q)
        oBloca = Bloca[:]
        oRloca = Rloca[:]
        for d in range(4):
            red = 0
            blue = 0
            flag = 1
            while flag:
                flag = 0
                if Bloca[0]+dy[d] != Rloca[0] or Bloca[1]+dx[d] != Rloca[1]:
                    if ([Bloca[0]+dy[d], Bloca[1]+dx[d]], Rloca) not in visited:
                        if board[Bloca[0]+dy[d]][Bloca[1]+dx[d]] == 'O':
                            blue = 1
                        elif board[Bloca[0]+dy[d]][Bloca[1]+dx[d]] != '#':
                            Bloca[0] += dy[d]
                            Bloca[1] += dx[d]
                            flag = 1
                            visited.append((Bloca, Rloca))
                        
            
            flag = 1
            while flag:
                flag = 0
                if Rloca[0]+dy[d] != Bloca[0] or Rloca[1]+dx[d] != Bloca[1]:
                    if (Bloca, [Rloca[0]+dy[d], Rloca[1]+dx[d]]) not in visited:
                        if board[Rloca[0]+dy[d]][Rloca[1]+dx[d]] == 'O':
                            red = 1
                            # 구멍에 빠진 이후 처리
                            Rloca[0] = 0
                            Rloca[1] = 0
                        elif board[Rloca[0]+dy[d]][Rloca[1]+dx[d]] != '#':
                            Rloca[0] += dy[d]
                            Rloca[1] += dx[d]
                            flag = 1
                            visited.append((Bloca, Rloca))
            
            flag = 1
            while flag:
                flag = 0
                if Bloca[0]+dy[d] != Rloca[0] or Bloca[1]+dx[d] != Rloca[1]:
                    if ([Bloca[0]+dy[d], Bloca[1]+dx[d]], Rloca) not in visited:
                        if board[Bloca[0]+dy[d]][Bloca[1]+dx[d]] == 'O':
                            blue = 1
                        elif board[Bloca[0]+dy[d]][Bloca[1]+dx[d]] != '#':
                            Bloca[0] += dy[d]
                            Bloca[1] += dx[d]
                            flag = 1
                            visited.append((Bloca, Rloca))
                                
            if blue == 0 and red == 0:
                q.append((Bloca, Rloca))
                print("여기서 다시 넣니")
                print(q)
                
            if blue == 0 and red == 1:
                q = []
                ans = cnt
                break

            Bloca = oBloca[:]
            Rloca = oRloca[:]

        if blue == 0 and red == 1:
            break

    lenq = len(q)

print(ans)
