"""
SWEA 3813 그래도 수명이 절반이 되어서는

input)
3
9 3
5 2 3 6 1 4 1 3 2
2 1 3
9 2
1 2 3 4 5 6 7 8 9
2 3
9 2
1 2 3 4 5 4 3 2 1
2 3

output)
#1 3
#2 5
#3 3

2019.09.19 PBY 완탐으로 짜보려다 그만둠
2019.09.25 PBY 해설참조 후 새로 작성
"""

# 이분탐색의 종료 조건은 어떻게 설정하는가?
# %2 로 짝수, 홀수를 나누지 않으면 3, 6, 3이 나온다. 종료 조건이 제대로 설정되지 않는다!

for testcase in range(int(input())):
    N, K = map(int, input().split())
    drives = list(map(int, input().split()))
    blocks = list(map(int, input().split()))

    # 이분탐색 알고리즘
    wears = list(set(drives))
    wears.sort()
    start = 0
    end = len(wears)-1
    middle = (start+end)//2+(start+end)%2

    flag = 0
    while flag == 0:
        c_ind = 0
        b_ind = 0
        for i in range(N):
            if drives[i] <= wears[middle]:
                c_ind += 1
            if c_ind >= blocks[b_ind]:
                b_ind +=1
                c_ind = 0 # 초기화

            # 다음 wear level 크기 결정
            if b_ind == K:
                last_poss = middle
                # middle을 더 작은 수로 변경
                end = middle
                middle = (start+end)//2+(start+end)%2
                if last_poss == middle:
                    flag = 1
                break
        else:
            # middle을 더 큰 수로 변경
            start = middle
            middle = (start+end)//2+(start+end)%2
            # 더 커질 수 없으면 while문 종료
            if middle == end:
                flag = 1
                break
    print(wears[last_poss])
    
# 완탐
"""
for testcase in range(int(input())):
    min_life = Inf # 큰 수로 대체
    N, K = map(int, input().split())
    drives = list(map(int, input().split()))
    blocks = list(map(int, input().split()))

    # 모든 조합 다 확인
    def combination(K, blocks, drives, k_ind, b_ind, minvalue):
        if b_ind > N-blocks[-1]:
            return
        current_max = max(blocks[b_ind:b_ind+K[k_ind]])
        minvalue = current_max if minvalue < current_max
        # 어떤 경우에 인덱스를 뒤로 미루고
        if k_ind < K and :
        # 어떤 경우에 다음 block을 선택?
"""
