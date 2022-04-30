"""
5 Twisty Little Passages

실행 방법
python interactive_runner.py python local_testing_tool.py 0 -- python 5_Twisty_Little_Passages.py
(cmd 창에서 실행할 때 리눅스가 아니라 python3 가 안 먹어서 python 으로 바꿨다)

아니면 이 파일을 실행해서 예제를 입력해보는 방법도 있다.
1
2 500
1 1
2 1
답 계산할 때 / 와 // 를 같이 쓰면 // 가 있어서 소수점이 없어진다고 생각했는데,
소수점이 나왔다. 그래서 전부 다 // 로 바꿔주었다.

input = sys.stdin.readline 하면 interactive runner가 안 돈다.
TLE 가 나온다.
"""

# wrong answer

#import sys
#input = sys.stdin.readline

for tc in range(int(input())):
    N, K = map(int, input().split())
    R, P = map(int, input().split())
    room = [-1]*N
    room[R-1] = P
    total = P
    count = 1
    last = 0
    for i in range(K):
        for j in range(last, N):
            if room[j] == -1:
                print(f"T {j+1}")
                R, P = map(int, input().split())
                room[R-1] = P
                total += P
                count += 1
                last = j+1
                break
        else:
            break

    print(f"E {total*N//2//count}")

"""
for tc in range(int(input())):
    N, K = map(int, input().split())
    R, P = map(int, input().split())
    room = [-1]*N
    room[R-1] = P
    total = P
    count = 1
    for i in range(K):
        for j in range(N):
            if room[j] == -1:
                print(f"T {j+1}")
                R, P = map(int, input().split())
                room[R-1] = P
                total += P
                count += 1
                break
        else:
            break

    print(f"E {total*N//2//count}")
"""
