"""
1233 주사위

brute force

정규분포를 따르지 않을까 싶어서
3개의 수 중 가장 min 값의 중간 * 3 이 되지 않을까 했는데 답과 달랐다
1 2 3
1 2 3 4
이렇게 둘을 더하면

2 3 4
3 4 5
4 5 6
5 6 7
이니까 가운데 2를 두 번 더한 4가 더 많아 보여서 그런 풀이를 생각했다.

하지만 문제 예제도 나오지 않아서 아래와 같이 완전 탐색으로 풀었다.
"""
S1, S2, S3 = map(int, input().split())
cnt = [0] * (S1*S2*S3 + 1)
_max, _cnt = 0, 0
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            _num = i+j+k
            cnt[_num] += 1
            if cnt[_num] > _cnt:
                _max = _num
                _cnt = cnt[_num]
print(_max)
