"""
20164 홀수 홀릭 호석

Brute Force
2021.11.24 부분 성공
2022.05.29 맞았습니다

헷갈렸던 부분은 문제에서 홀수의 개수를 세라고 했을 때,
모든 수를 다 확인하는 건지, 두 자리수로 잘렸을 때 마지막 숫자만 확인하는 건지
헷갈렸는데 예제를 출력해보고 알았다.
"""

# 통과 (2022.05.29)
# 3개로 분할할 때 i, j, k 가 아닌 i,j 만 사용해야함
import sys
sys.setrecursionlimit(100000000)

def recur(st, cur):
    global _min, _max

    temp = 0
    for s in st:
        if int(s) % 2:
            temp += 1

    _len = len(st)
    
    if _len <= 1:
        _min = min(_min, cur + temp)
        _max = max(_max, cur + temp)
        return

    if _len <= 2:
        recur(str(int(st[0])+int(st[1])), cur+temp)
        return

    for i in range(1,_len):
        for j in range(i+1, _len):
            recur(str(int(st[:i])+int(st[i:j])+int(st[j:])), cur+temp)
            

N = input()
_min = 1000000000
_max = 0 # 9 * log 9 ?

recur(N, 0)
print(_min, _max)

# 부분 성공 (2021.11.24)
"""
def recur(st, cur):
    global _min, _max

    temp = 0
    for s in st:
        if int(s) % 2:
            temp += 1

    _len = len(st)
    #print("###", st, temp, _len)
    
    if _len <= 1:
        _min = min(_min, cur + temp)
        _max = max(_max, cur + temp)
        return

    if _len <= 2:
        recur(str(int(st[0])+int(st[1])), cur+temp)
        return

    for i in range(_len-2):
        for j in range(i+1, _len-1):
            for k in range(j+1, _len):
                recur(str(int(st[i:j])+int(st[j:k])+int(st[k:])), cur+temp)
            

N = input()
_min = 1000
_max = 0 # 9 * log 9 ?

recur(N, 0)
print(_min, _max)
"""
