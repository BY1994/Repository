
"""
보충수업_ SW expert 요리사

190308 PBY 최초작성
"""

T = int(input()) # 테스트케이스
for tc in range(T):
    N = int(input()) # 식재료의 수
    sinerge = []
    for _ in range(N):
        sinerge.append(list(map(int, input().split())))
    Ns = list(range(N))
    
    minvalue = 20000

    
    for i in range(1 << N):
        tempB = []
        tempA = []
        for j in range(N):
            if i & (1 << j):
                tempB.append(Ns[j])
            else: # 0에 해당하는 부분 넣기
                tempA.append(Ns[j])
        # j와 다 비교를 해서 넣었을 때,
        # 개수가 N//2개여야함
        if len(tempB) == N//2:
            tasteA = tasteB = 0
            for i2 in range(N//2):
                for j2 in range(N//2):
                    if i2 == j2:
                        continue
                    tasteA += sinerge[tempA[i2]][tempA[j2]]
                    tasteB += sinerge[tempB[i2]][tempB[j2]]

            if abs(tasteA - tasteB) < minvalue:
                minvalue = abs(tasteA - tasteB)

    print("#%d %d" %(tc+1, minvalue))


"""                
    # 시너지 받고 음식 2개 선택 = > N//2 를 선택해야함
    for i in range(N):
        for j in range(N):
            if i == j: # 본인은 건너뛰고
                continue
            B = list(range(N)) #[0, 1 ,2, 3]
            newB = []
            for item in range(N): # B의 개수
                if B[item] != i and B[item] != j:
                    newB.append(B[item])
            # i랑 j가 선택됨
            tasteA = sinerge[i][j] + sinerge[j][i]
            tasteB = sinerge[newB[0]][newB[1]] + sinerge[newB[1]][newB[0]]

            # A와 B의 차이 비교
            if abs(tasteA - tasteB) < minvalue:
                minvalue = abs(tasteA - tasteB)

    print("#%d %d" %(tc+1, minvalue))
"""

"""
N개 중에
N(n/2 x n/2 ( n/2

16 ( 8 나머지가 자연스럽게 나옴

조합은 부분집합과 관련이 있다.
최대 원소의 개수가 16개일 때, 부분집합의 원소의 개수가 8개인 부분집합을 찾아내는 문제이다.

바이너리 카운팅으로 모든 부분집합 만들 수 있다.
-> 바이너리 카운팅으로 만들 수 있다.

백준 퇴사
"""


"""
N = int(input()) # N이 원소의 개수
lst = list(range(N))

for subset in range(1, (1 << N)): # N만큼 시프트하면 2의 N승이 되니까 바이너리 카운팅
    cnt = 0
    for i in range(N): # subset은 정수형 변수, N개의 하이비트를 쓰는데, 1이 몇 개인지 따라서 부분집합 원소의 개수 알 수 있다.
        if subset & (1 << i):
            cnt += 1
    
    A, B = [], []
    if cnt == N//2:
        for i in range(N): 
            if subset & (1 << i): A.append(i)
            else: B.append(i)
        print(A, B)
"""


"""
arr=[2, 6, 7 ,1, 5, 4]
n = 4#len(arr)
for i in range(1<<n):
    for j in range(n+1):
        if i & (1 << j):
            print(arr[j], end=", ")
    print()
print()
"""
