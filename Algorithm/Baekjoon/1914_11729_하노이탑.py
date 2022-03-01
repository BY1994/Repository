"""
1914 하노이 탑
11729 하노이 탑

  -
 __
___

 1         2      3
(start) (temp)  (end)

마지막 원판을 제외하고 나머지가 temp 로 가야,
end 위치에 마지막 원판을 두고 temp 에 있던 나머지가 또 end 로 올라올 수 있음

재귀로 들어가면 그때그때 start 부터 destination 이 달라짐
"""

def hanoi(start, end, temp, disc):
    if disc == 1:
        print(start, end)
    else:
        hanoi(start, temp, end, disc-1)
        print(start, end)
        hanoi(temp, end, start, disc-1)

N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(1, 3, 2, N)

"""
def hanoi(start, end, temp, disc):
    if disc == 1:
        print(start, end)
    else:
        hanoi(start, temp, end, disc-1)
        print(start, end)
        hanoi(temp, end, start, disc-1)

N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(1, 2, 3, N-1)
    print(1, 3)
    hanoi(2, 3, 1, N-1)
"""
