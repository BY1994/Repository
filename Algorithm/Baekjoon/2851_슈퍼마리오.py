""" 
2851 슈퍼 마리오
문제 내용
슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.
슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다.
중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.
마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.
버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오. 

[입력]
총 10개의 줄에 각각의 버섯의 점수가 주어진다. 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.

[출력]
첫째 줄에 마리오가 받는 점수를 출력한다. 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.

"""

scores = []
for score in range(10):
    # input 받기
    scores.append(int(input()))

# 100과의 차이
diff = 100
score = 0

for length in range(1, 11):
    # length에 따라 start와 end가 결정됨
    # 100과의 차이가 작아야 저장
    cur_sum = sum(scores[:length])
    if diff >= abs(100-cur_sum):
        if score < cur_sum:
            score = cur_sum
            diff = abs(100-cur_sum)
    # 구간의 길이에 따라 맞는 시작점을 가지고
    # 구간합을 구하면서, 100과의 차이가 작아야 저장한다.
print(score)

"""
start 지점은 변하지 않는다.... ㅠㅠ 아래는 구간합으로 오해한 풀이


# 전체 구간의 길이를 다르게 잡고,
for length in range(1, 11):
    for start in range(0, 10-length+1):
        # length에 따라 start와 end가 결정됨
        # 100과의 차이가 작아야 저장
        cur_sum = sum(scores[start:start+length])
        if diff >= abs(100-cur_sum):
            if score < cur_sum:
                score = cur_sum
                diff = abs(100-cur_sum)
    # 구간의 길이에 따라 맞는 시작점을 가지고
    # 구간합을 구하면서, 100과의 차이가 작아야 저장한다.
print(score)
"""
# visual studio는 실행시 ctrl + f5
