"""
백준 알고리즘 2448
백준 Online Judge - 문제 - 단계별로 풀어보기 - 함수 사용하기 - 별 찍기 - 11

문제)
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력)
첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (k ≤ 10)
24

출력)
첫째 줄부터 N번째 줄까지 별을 출력한다.

최초 작성 2019.01.23 PBY
최종 제출 2019.01.24 PBY
"""

# input
N = 24 #int(input())

# total_range 의 크기는 별 5개 x 3 나누기 한 개수 + 3나누기한 개수 -1(=공백 개수)
total_range = [[' ' for c in range(5*int(N/3) + int(N/3)-1)] for r in range(N)]

# 시작점 리스트 초기화
slist = [0, len(total_range[0])+1]

# 거꾸로 가면서 밑에서부터 *을 찍는다.
for row in range(N-1, -1, -1):
    news = [] # 다음 시작점 리스트

    if (row+1) % 3 == 0: # ***** 의 경우
        for idx, s in enumerate(slist): # 시작점:끝점 사이에 *****을 채울 수 있는 만큼 채운다.
            if idx % 2 == 0:
                total_range[row][slist[idx]: slist[idx+1]] = (['*']*5+[' ']) * ((slist[idx+1]-slist[idx])//6)
                # * * 의 경우를 위한 다음 시작점 업데이트
                for i in range(0, (slist[idx+1]-slist[idx])//6):
                    news.extend([slist[idx]+1 + i*6, slist[idx]+3+i*6])

    # 다른 애들은 표시한 시작점에 '*'을 넣어주면 됨
    elif (row+1) % 3 == 2: # * *의 경우
        for idx, s in enumerate(slist):
            total_range[row][s] = '*'
            # 시작점 업데이트 ( 다음 별 * 하나 찍을 자리)
            if idx % 2 == 0: # * * 이 사이에 찍어줘야함
                news.append(s+1)

    elif (row+1) % 3 == 1: # * 의 경우
        for idx, s in enumerate(slist):
            total_range[row][s] = '*'
            # 다음 시작점을 위한 업데이트
            news.append(s+1) # *의 시작점과 끝점을 알려주기 위해 지금 찍은 자리 알려줌
    slist = news[:]

# 별 프린트
for row in range(len(total_range)):
    print(''.join(total_range[row]))

