"""
2491 수열

2019.03.07 PBY 최초작성
"""

N = int(input())
numbers = list(map(int, input().split()))

# 커지는 숫자 확인
flag = 0
maxlength = 1 # default값은 1로 잡아줘야 하지 않나. 나 혼자 수열인 경우를 생각해서!!
for idx in range(N-1):
    if numbers[idx] <= numbers[idx+1]:
        if flag == 0:
            start = idx
            flag = 1
    else:
        if flag == 1:
            end = idx
            flag = 0
            # end를 찾으면 그때 max인지 비교
            if maxlength < end-start+1:
                maxlength = end-start+1

# 혹은 맨 끝까지 갔을 때 max인지 비교
if flag == 1:
    if maxlength < N-1-start + 1:
        maxlength = N-1-start + 1 # 오타 미쳤다.....

# 작아지는 숫자 확인
flag = 0
for idx in range(N-1):
    if numbers[idx] >= numbers[idx+1]:
        if flag == 0:
            start = idx
            flag = 1
    else:
        if flag == 1:
            end = idx
            flag = 0
            if maxlength < end-start + 1:
                maxlength = end-start + 1
if flag == 1:
    if maxlength < N-1 - start + 1:
        maxlength = N-1 - start + 1

print(maxlength)

"""
# 틀렸습니다 1 
문제를 잘못 이해해서 3 보다 작으면 2를 출력하라는 줄 알았다.

if maxlength < 3:
    print(2)
else:
    print(maxlength)
"""

"""
# 틀렸습니다 2
for문 안에서만 maxlength를 업데이트 해서 수열이 끝까지 규칙성을 유지한 경우에는 세지 않았다.

"""

"""
# 틀렸습니다 3
질문 목록을 봤는데, 1 1 인 경우에는 2가 아닌 1 이 출력되어야 하고, 1을 넣으면 1이 출력되어야한다고 한다.
=> 아니 내 코드는 2 \n 1 2 가 들어가면 0이 출력된다?!
=> 미쳤다!!!!!!!!!!!!!!!!!!! 오타!!!!!!!!!!!!!!!!!!!
maxlength를 maxlegnth라고 하나 잘못 썼는데, 오류 없이 돌아갔다!!!!!!!!!!!!!!
심지어 채점도 100%까지 돌아갔다!!!!!!!!!!!!!!!
"""