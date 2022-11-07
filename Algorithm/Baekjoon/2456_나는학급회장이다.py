"""
2456 나는 학급회장이다

구현, 많은 조건 분기
난이도가 브론즈 1인 이유는 같은 점수인 후보가 2 이상일 때, 계속 분기가 들어가기 때문

아래 코드 더 최적화 가능
total + cnt 를 하나의 배열로 합칠 수 있다. 그러면 두 개 로직을 분리할 필요가 없다.
참고 코드: https://www.acmicpc.net/source/16674663
"""

def get_max_id():
    candidate = [0]*3
    c_num = 0
    _max = 0

    for i in range(3):
        if total[i] > _max:
            _max = total[i]
            candidate[0] = i
            c_num = 1
        elif total[i] == _max:
            candidate[c_num] = i
            c_num += 1

    if c_num == 1:
        return candidate[0]+1

    for score in range(3, 0, -1):
        _max = 0
        prev_cand = candidate[:c_num]
        c_num = 0
        for i in prev_cand:
            if cnt[i][score] > _max:
                _max = cnt[i][score]
                candidate[0] = i
                c_num = 1
            elif cnt[i][score] == _max:
                candidate[c_num] = i
                c_num += 1

        if c_num == 1:
            return candidate[0]+1

    return 0

N = int(input())
total = [0]*3
cnt = [[0 for i in range(4)] for j in range(3)]
for i in range(N):
    s = list(map(int, input().split()))
    for j in range(3):
        cnt[j][s[j]] += 1
        total[j] += s[j]

print(get_max_id(), max(total))
