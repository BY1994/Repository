"""
한윤정이 이탈리아에 가서 아이스크림을 사먹는데

2019.04.15
"""

N, M = map(int, input().split())

# 인접 리스트로 만들기
icecreams = [[] for _ in range(N)]

for _ in range(M):
    icea, iceb = map(int, input().split())
    #icecreams[icea] += 1; icecreams[iceb] += 1
    icecreams[icea-1].append(iceb-1); icecreams[iceb-1].append(icea-1)
    
# 조합 만들기
used = [False] * N
comb = [0] * 3 # 아이스크림 3개 선택하기
cnt = 0

def combination(depth, selected):
    global cnt, N
    if depth == 3: # 3개를 선택했으면
        cnt += 1
        return

    # 앞에 선택한 애들을 다 돌면서 안 되는 애 아닌 애를 선택한다.
    for u in range(selected, N):
        if used[u] == False: # 선택하려면 일단 선택이 안 되어있어야한다.
            for i in range(depth):
                if u in icecreams[comb[i]]: # 사용하고자 하는 애가 거기에 들어있으면
                    break
            else: # 아무도 들어있지 않아야
                used[u] = True # 선택하고
                comb[depth] = u # 넣어주고
                combination(depth+1, u+1)
                used[u] = False

combination(0, 0)
print(cnt)
