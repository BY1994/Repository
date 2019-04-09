# DP로 구현해보기

def countpipes(x, y):
    global N
    m = 0
    for d in range(3): # y가 끝에 닿은 경우 아래로 내려갈 수가 없다!!!! N-1로 해준다.
        if 0<=x+dx[d]<N and 0<=y+dy[d]<N-1 and type(pipes[x+dx[d]][y+dy[d]])==int:
            m += pipes[x+dx[d]][y+dy[d]]
    return m

dx = [-1, -1, 0] # 위, 대각선, 왼쪽
dy = [0, -1, -1] 
N = int(input())
pipes = []
for _ in range(N):
    pipes.append(input().split())

pipes[0][1] = 1 # 가로로 한 칸 갈 수 있는 것
pipes[1][1] = 0 # 아래로 갈 수 없음
pipes[0][2] = 1 # 가로로 한 칸 갈 수 있음

# 대각선 탐색 세로
for i in range(3, N): # 2 지점은 직접 넣어줘야할 듯
    for k in range(i, -1, -1):
        pipes[i-k][k] = countpipes(i-k, k)
        
# 대각선 탐색 가로
for j in range(1, N):
    print("j", j)
    for k in range(N-j):
        print("k", k)
        print(j+k, N-k-1)
        
        pipes[j+k][N-1-k] = countpipes(j+k,N-k-1)
        
print(pipes[N-1][N-1])
