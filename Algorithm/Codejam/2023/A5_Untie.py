"""
Codejam2023 A round
Untie

종이에 써보고 규칙을 찾아서 그대로 솔루션 구현
가운데 낀 문자를 생각해보면
PRP 1개일 때는 0 개 교환
PRRP 2개일 때는 1개 교환
PRRRP 3개일 때는 1개 교환
PRRRRP 4개일 때는 2개 교환
이런 식으로 개수 // 2 로 식이 생긴다.

맨 앞과 맨 뒤로 연결된 문자는 처리하기 복잡해서 if 로 빼서 초반에 처리해두었다.
이걸 이용해서 start 와 end 범위를 안쪽으로 좁혀두었다.

그리고 완전히 같은 문자열만 있는 경우는 위의 규칙과 다른데
R 은 0개 교환
RR 은 1개 교환
RRR 은 2개 교환
RRRR 은 2개 교환
RRRRR 은 3개 교환
으로 R 의 개수 // 2 + R의 개수 % 2 로 식이 생긴다.
"""

for tc in range(int(input())):
    S = input()
    ans = 0
    # 연속으로 중복된 게 몇 개인지 세기
    neighbor = 1
    N = len(S)
    start = -1
    end = N-1
    if N > 1 and S[N-1] == S[0]:
        # start, end 찾기
        for i in range(N-1):
            if S[i+1] == S[i]:
                neighbor += 1
                start = i+1
            else:
                break
        for i in range(N-1, start, -1):
            neighbor += 1            
            if S[i-1] == S[i]:
                end = i-1
            else:
                break
    if N > 1 and N == neighbor:
        print(f"Case #{tc+1}: {neighbor//2 + neighbor%2}")
        continue
    
    ans += neighbor//2
    neighbor = 1
    for i in range(start+1, end):
        if S[i+1] == S[i]:
            neighbor += 1
        else:
            ans += neighbor//2
            neighbor = 1
    ans += neighbor//2
    print(f"Case #{tc+1}: {ans}")
