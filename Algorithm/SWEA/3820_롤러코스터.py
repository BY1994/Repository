"""
3820 롤러코스터

2019.09.27 PBY 해설보고 작성
"""

for testcase in range(int(input())):

    # input
    N = int(input())
    rails = []
    rails_v = [0]*N
    for i in range(N):
        rails.append(list(map(int, input().split())))
        rails_v[i] = (rails[i][0]-1)/rails[i][1]


    # proof
    index = sorted(range(N), key=lambda k:rails_v[k], reverse=True)

    # sort 결과물대로 계산 => 총 얼마걸리는지
    v = 1
    for i in range(N):
        v = rails[index[i]][0]*v + rails[index[i]][1]
    
    # 100007 나누기?
    print('#%d %d' %(testcase+1, v%1000000007))
