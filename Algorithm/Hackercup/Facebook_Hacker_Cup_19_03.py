"""
facebook Hacker Cup 2019 Qualification Round 
Mr.X

Input)
4
X
0
(x|1)
((1^(X&X))|x)

2019.06.15 PBY 최초 작성
"""

# input
T = int(input())
for case in range(T):
    question = input()

    # ans1
    x = 1
    X = 0
    ans1 = eval(question)

    # ans2
    x = 0
    X = 1
    ans2 = eval(question)

    # compare
    if ans1 == ans2:
        ans = 0
    else:
        ans = 1
    print("Case #%d: %s" %(case+1, ans))


"""
valid, invalid 컨셉을 보면 3글자가 되면 무조건 () 에 들어가야 하기 때문에,
마지막은 결국 무언가 or 무언가 혹은 무언가 and 무언가 이런 식일 것이다.
그러면 결국 요약은 둘이 같은 값이거나 다른 값이 될 것이다.
true, false로 x input값을 바꿔도 차이가 없으면 0
true, false로 바꿔넣었을 때 차이가 생기면 가장 가운데 기호만 바꿔서 1

true인 경우 11이고 false인 경우에 10이라면? or을 넣으면 될 것
true인 경우 11이고 false인 경우에 00이라면? xor을 넣으면 될 것
"""
