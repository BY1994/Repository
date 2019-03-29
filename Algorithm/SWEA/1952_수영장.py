

def usePool(month, cur_sum):
    global minvalue
    if cur_sum > minvalue: # 가지치기
        return
    if month >= 13: # 마지막 달
        if minvalue > cur_sum:
            minvalue = cur_sum
        return

    # 3달짜리
    usePool(month+3, cur_sum+costs[2])
    usePool(month+1, cur_sum+costs[1])
    usePool(month+1, cur_sum+costs[0]*months[month-1])

T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    months = list(map(int, input().split()))

    minvalue = costs[-1]
    # 재귀함수 호출
    # 3달짜리
    usePool(4, costs[2])
    # 1달짜리
    usePool(2, costs[1])
    usePool(2, costs[0]*months[0])
    print("#%d %d" %(tc+1, minvalue))
