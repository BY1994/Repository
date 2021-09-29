"""
Codeforces Round #744 (Div.3)
B

제일 작은 수부터 맨 앞으로 보내기 위해서
맨 앞 자리랑 (정렬된 맨 앞자리) 제일 작은 수 범위를 잡고
제일 작은 수가 맨 앞에 오도록 shift를 한다
그건 둘의 인덱스 차이랑 같다

최단 횟수를 구하는 문제가 아니라
이렇게 하면 최악의 경우 n 번 제한 안에 들어온다.

"""

tc = int(input())
for _ in range(tc):
    ans = []
    ansn = 0
    n = int(input())
    array = list(map(int, input().split()))

    for i in range(n):
        small = i
        for k in range(i, n):
            if array[k] <= array[small]:
                small = k
        # if my location is correct, do nothing
        if small > i:
            d = small - i
            end = array[small]
            for m in range(small, i, -1):
                array[m] = array[m-1]
            array[i] = end
            ansn += 1
            ans.append([i+1, small+1, d])
        #print("###")
        #print(*array, sep=" ")
    print(ansn)
    for j in range(ansn):
        print(*ans[j], sep = " ")
    
