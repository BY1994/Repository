"""
1436 영화감독 숌

log N 풀이를 위해 재도전하면 좋을 것 같다.
"""

def check(num):
    return '666' in str(num)

N = int(input())
count = 0
for i in range(666, 6660002):
    if check(i):
        count += 1
    if count == N:
        print(i)
        break

# C언어 풀이
#https://www.acmicpc.net/source/30135855

# Python 풀이
# https://www.acmicpc.net/source/18295061
# https://www.acmicpc.net/source/15406501
