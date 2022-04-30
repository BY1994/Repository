"""
1
2
ABCDEFGHI A
Case #1: IMPOSSIBLE

# => 급하게 위의 반례 해결했지만 WA

답안을 보니
후보군을 찾고
그 후보군에서부터 가능한 연결해보고
최종 가능하면 답으로 출력

아니면 IMPOSSIBLE

sample 1 만 맞추려면
후보군도 안 찾고
그냥 모든 거를 시작점으로 두고 가능한 연결하는 거
"""

T = int(input())
for tc in range(T):
    alpha = [0] * 26
    N = int(input())
    words = input().split()

    # 내가 누구의 끝과도 연결되지 않는 거 찾기
    # 그러면서 내 끝이 누군가의 시작점인 거
    flag = 0
    ind = 0
    for i in range(N):
        flag = 0
        start = words[i][0]
        for j in range(N):
            if i == j: continue
            if words[j][-1] == start:
                # 5 번 케이스 때문에 조건문 하나 더 추가
                if len(words[j]) > 1 and words[j][-1] != words[j][0]:
                    flag = 1
                    break
                elif len(words[j]) == 1:
                    flag = 1
                    break
        if flag == 0:
            # 그러면서 내 끝이 누군가의 시작점인 거 => 필요 없을 듯 밑에 while문 덕분에 
            # 5번 케이스 때문에 처리 필요해짐  -> ?
            ind = i
            break
    # start
    ans = ''
    ans += words[ind]
    last = words[ind][-1]
    words[ind] = -1
    flag = 0
    while True:
        pos = -1
        flag = 0
        for i in range(N):
            if words[i] == -1:
                continue
            if words[i][0] == last:
                if words[i][0] == words[i][-1]:
                    ans += words[i]
                    words[i] = -1
                else:
                    pos = i
                flag = 1

        if pos != -1:
            ans += words[pos]
            last = words[pos][-1]
            words[pos] = -1

        # 다음에 넣을 게 끊기면?
        if flag == 0:
            flag2 = 0
            ind = 0
            for i in range(N):
                if words[i] == -1:
                    continue
                ind = i # 초기화
                flag2 = 0
                start = words[i][0]
                for j in range(N):
                    if i == j: continue
                    if words[j] == -1:
                        continue
                    if words[j][-1] == start:
                        # 5번 케이스 고려해서 하나 추가
                        if words[j][0] != words[j][-1]:
                            flag2 = 1
                            break
                if flag2 == 0:
                    ind = i
                    break

            if words[ind] == -1:
                break

            ans += words[ind]
            last = words[ind][-1]
            words[ind] = -1

    # check
    ordA = ord('A')
    prev = ord(ans[0])-ordA
    flag = 0
    for i in range(1, len(ans)):
        if ord(ans[i])-ordA != prev:
            if alpha[prev] != 0:
                # impossible
                flag = 1
                break
            alpha[prev] = 1
            prev = ord(ans[i])-ordA

    if alpha[prev] != 0: # 마지막 글자
        # impossible
        flag = 1

    if flag == 1:
        print(f"Case #{tc+1}: IMPOSSIBLE")
    else:
        print(f"Case #{tc+1}: {ans}")
        
"""
for tc in range(T):
    start = [-1]*26
    end = [-1]*26
    both = [-1]*26
    alpha = [0]*26
    N = int(input())
    words = input().split()

    # alpha 에 있는데 start 나 end 나 both 에 나오면 IMPOSSIBLE

    for i in range(N):
        # start 아닌 애 나올 때까지
        # end 아닌 애 나올 때까지
        
        
        if words[i]

    # 내가 누구의 시작점도 아닌 거 찾기
    flag = 0
    ind = -1
    for i in range(N):
        flag = 0
        start = words[i][0]
        for j in range(N):
            if i == j: continue
            if words[j][-1] == start:
                flag = 1
                break
        if flag == 0:
            ind = i
            break
    if ind == -1:
        print(f"Case #{tc+1}: IMPOSSIBLE")
    else:
        while True:
            words[ind]
"""

"""
for tc in range(T):
    alpha = [0] * 26
    N = int(input())
    words = input().split()
    # 내가 누구의 시작점도 아닌 거 찾기
    flag = 0
    ind = -1
    for i in range(N):
        flag = 0
        start = words[i][0]
        for j in range(N):
            if i == j: continue
            if words[j][-1] == start:
                flag = 1
                break
        if flag == 0:
            ind = i
            break
    if ind == -1:
        print(f"Case #{tc+1}: IMPOSSIBLE")
    else:
        while True:
            words[ind]
"""
