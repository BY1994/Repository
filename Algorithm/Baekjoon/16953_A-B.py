"""
16953 A->B

그리디, 끝에 1이 붙는 경우는 2를 곱해서는 절대 만들 수 없음

최초 풀이 2022.03.24 (not submitted)
새로 품 2022.07.05 (submitted)
"""
# 2022.07.05 풀이 버전
A, B = map(int, input().split())
ans = 0
while B > A:
    if B % 10 == 1:
        B //= 10
        ans += 1
    elif B % 2 == 0:
        B //= 2
        ans += 1
    else:
        break

if B == A:
    print(ans+1)
else:
    print(-1)


# 2022.03.24 풀이 버전
"""
ans = 1
A, B = map(int, input().split())
while A!=B:
    if B % 10 == 1:
        B //= 10
        ans += 1
    elif B % 2 == 0:
        B //= 2
        ans += 1
    else:
        print(-1)
        break

    if A > B:
        print(-1)
        break
else:
    print(ans)
"""
