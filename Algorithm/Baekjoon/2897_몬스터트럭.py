"""
2897 몬스터 트럭

brute force

python 시간 1등
누적합을 사용하는 방법도 있을 것 같다.
C 언어라면 hash 가 아닌 배열로 #, ., X를 접근했겠지만
python 은 dict 가 빠를 것 같아서 이렇게 구현하였다.
"""
R, C = map(int, input().split())
park = []
cnt = {'#':0, '.':0, 'X':0}
for i in range(R):
    park.append(input())
ans = [0] * 5
for i in range(R-1):
    for j in range(C-1):
        cnt['#'] = 0
        cnt['.'] = 0
        cnt['X'] = 0

        cnt[park[i][j]] += 1
        cnt[park[i][j+1]] += 1
        cnt[park[i+1][j]] += 1
        cnt[park[i+1][j+1]] += 1
        if cnt['#'] > 0:
            continue
        else:
            ans[cnt['X']] += 1

for i in range(5):
    print(ans[i])
