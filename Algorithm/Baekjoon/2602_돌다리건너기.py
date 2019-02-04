"""
백준 2602 돌다리 건너기

20190127 PBY 최초작성
"""

# input
duru = input()  # 'RGS'
dari1 = input()  # 'RINGSR'
dari2 = input()  # 'GRGGNS'

# 필요한 리스트 만들기
# duru에 있는 애들 위치를 dari1에서 찾는다.
def possibleRoute(dari1, dari2):
    # 1개만 있는 경우
    if len(duru) == 1:  # 1개만 있는 경우
        return dari1.count(duru[0])

    dari_list1 = [[] for i in range(len(duru[::2]))]
    dari_list2 = []
    for idx, d in enumerate(duru[::2]):
        for idx2, i in enumerate(dari1): # d에 해당하는 위치를 다 넣음
            if d == i: # R이 dari1에 있는 위치들, G가 dari1에 있는 위치들...
                dari_list1[idx].append(idx2)
                dari_list2.append(idx2) # [] 구분 없이 다 넣는 것

    # 부분집합 만들기
    total = 0
    for i in range(1 << len(dari_list2)): # 가능한 조합들
        subdari = [] # 현재 조합을 저장
        for j in range(len(dari_list2)):
            if i & (1 << j):
                subdari.append(dari_list2[j])

        # subdari를 돌면서 확인
        num = 0
        for j in range(len(subdari)):

            # subdari 는 dari_list1의 [] 안에 있어야함
            if subdari[j] not in dari_list1[j]: # 끝까지 못 도는 거 아냐??
                break
            else:
                # 다음 돌다리의 문자 개수 곱함
                if len(subdari) > 1 and j == 0: # 1개 이상이고, break하지 않은 경우
                    num = 1 # 한 가지 경우 존재한다고 가정
                if j != len(subdari)-1: # 마지막값이 아닐 때만
                    num *= dari2[subdari[j]+1:subdari[j+1]].count(duru[1::2][j])
                # duru가 짝수인 경우 (다음 돌다리에서 끝나는 경우)
                if (j == len(subdari)-1) and (len(duru) % 2 == 0):
                    num *= dari2[subdari[j]+1:].count(duru[-1])

        else:
            total += num

    return total

# 지금은 돌다리 개수가 홀수인 경우만 풀리는 것 같은데?

d1 = possibleRoute(dari1, dari2)
d2 = possibleRoute(dari2, dari1)

print(d1+d2)

# 부분 집합 안에서 현재 i가 dari_list[i인덱스에 있는지 찾고,
# 있으면 지금이 두번째 이상이면
# 그리고 이전과 다음 위치가 크기 순서가 < 이면
# 이전 위치와 지금 위치 사이에
# 다음 돌다리에서 duru 두번째 이상 문자의 개수를 세서 곱한다.