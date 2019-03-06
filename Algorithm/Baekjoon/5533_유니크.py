""" 
5533 유니크
문제 내용)
상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.
각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 참가자의 수 N이 주어진다. (2 ≤ N ≤ 200) 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.

출력)
각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.

최초작성 2019.03.05 PBY
"""

players = int(input())
inputs = [[0 for _ in range(players)] for __ in range(3)]
scores = [0 for _ in range(players)]

# 인풋 가로로 받기
for i in range(players):
    cur_input = list(map(int, input().split()))
    inputs[0][i] = cur_input[0]
    inputs[1][i] = cur_input[1]
    inputs[2][i] = cur_input[2]
    
# 점수 체크
for game in range(3):
    for player in range(players):
        if inputs[game].count(inputs[game][player]) > 1: # 겹치는 사람 있으면
            scores[player] += 0
        else:
            scores[player] += inputs[game][player]

# 점수 출력
for player in range(players):
    print(scores[player])

    
# visual studio는 실행시 ctrl + f5

