"""
17205 진우의 비밀번호

값이 없는 경우가 있으므로 27 x => 없다가 있다가 하는 건 없음
ans += 1 으로 현재 자리까지만 있고 멈춘 경우 고려!

diff 를 더해주는 건 없는 경우를 고려해줌
첫 번째 자리가 없는 경우 (c라면 a~b 까지만 존재하는 경우)
그 뒤는 등비수열의 합 (a~z = 26 + a~z x a~z = 26+26 ...)
그래서 등비수열의 합 + diff 로 식을 씀
"""

N = int(input())
pwd = input()
ans = 0
anum = ord('a')
N -= 1
for alpha in pwd:
    diff = ord(alpha) - anum
    if diff > 0:
        #ans += (ord(alpha) - anum)*(26**(N))
        #ans += (ord(alpha) - anum)*(26*(26**N) - 26)//(25)
        ans += (diff)*26*(26**N-1)//(25) + diff
    #else: ans += 1
    ans += 1
    N -= 1
print(ans)    

