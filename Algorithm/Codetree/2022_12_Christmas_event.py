"""
코드트리 크리스마스 이벤트
4문제 성공해서 연탄 4장 기부
"""

# 메리크리스마스
'''
print("""##  ##     ##     #####    #####    ##  ##            ##  ##            ##   ##    ##      ####
##  ##    ####    ##  ##   ##  ##   ##  ##            ##  ##            ### ###   ####    ##  ##
##  ##   ##  ##   ##  ##   ##  ##   ##  ##             ####             #######  ##  ##   ##
######   ######   #####    #####     ####               ##     ######   ## # ##  ######    ####
##  ##   ##  ##   ##       ##         ##               ####             ##   ##  ##  ##       ##
##  ##   ##  ##   ##       ##         ##              ##  ##            ##   ##  ##  ##   ##  ##
##  ##   ##  ##   ##       ##         ##              ##  ##            ##   ##  ##  ##    ####""")
'''

# 연탄 배달의 시작
# 완전 탐색
"""
#include <stdio.h>

int house[1001];

int main() {
    int N;
    int min = 1000010;
    int ans;
    scanf("%d", &N);
    scanf("%d", &house[0]);
    for (int i = 1; i < N; ++i) {
        scanf("%d", &house[i]);
        if (house[i] - house[i-1] < min) {
            min = house[i] - house[i-1];
            ans = 1;
        }
        else if (house[i] - house[i-1] == min) ans++;
    }
    printf("%d\n", ans);
    return 0;
}
"""

# 연탄의 크기
# 완전 탐색
"""
n = int(input())
house = list(map(int, input().split()))
ans = 0
for i in range(2,max(house)+1):
    temp = 0
    for j in range(n):
        if house[j] % i == 0:
            temp += 1
    if ans < temp:
        ans = temp
print(ans)
"""

# 루돌프 월드컵
# 완전 탐색
"""
import sys
sys.setrecursionlimit(1000000)

score_table = [[0 for i in range(4)] for j in range(4)]
F = list(map(int, input().split()))
ans = 0.0

def count(x, y, prob):
    global ans
    if x == 3 and y == 3:
        score = [0]*4
        # 승점 계산해서 1번 루돌프가 승인지
        # 1번 루돌프 점수를 이긴 사람이 2명 이상이어야함
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                if score_table[i][j] == 1:
                    score[i] += 3
                elif score_table[i][j] == 2:
                    score[i] += 1
        cnt = 0
        for i in range(1,4):
            if score[i] > score[0]:
                cnt += 1
        if cnt < 2:
            ans += prob
        return
    nx = x
    ny = y+1
    if x == y:
        nx = x
        ny = y+1
        if y == 3:
            nx = x + 1
            ny = 0
        count(nx, ny, prob)
        return
    if y == 3:
        nx = x+1
        ny = 0
    score_table[x][y] = 1 # 승
    score_table[y][x] = 3
    count(nx, ny, prob*(4*F[x]/(5*F[x] + 5*F[y])))
    score_table[x][y] = 2 # 무
    score_table[y][x] = 2
    count(nx, ny, prob*((F[x]+F[y])/(5*F[x]+5*F[y])))
    score_table[x][y] = 3 # 패
    score_table[y][x] = 1
    count(nx, ny, prob*(4*F[y]/(5*F[x]+5*F[y])))

count(0, 1, 1)
print(f'{ans*100:.3f}')
"""
