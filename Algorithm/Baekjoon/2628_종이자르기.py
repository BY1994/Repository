""" 
2628 종이자르기
문제 내용)
아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

입력)
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

출력)
첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

+
한국정보올림피아드 > KOI 2001 > 초등부 1번 (IM수준)

2019.03.05 PBY 최초작성

"""

#import sys
#sys.stdin = open('C:/Users/student/TIL/Algorithm/Baekjoon/1244_input.txt','r')

paper = input().split()
scissors = int(input())
hori = [0] # 여기 시작점과
verti = [0]
for _ in range(scissors):
    cur_input = input().split()
    if cur_input[0] == '0': # 가로선
        hori.append(int(cur_input[1]))
    else:
        verti.append(int(cur_input[1]))
hori.append(int(paper[1])) # 여기 끝 점을 안 넣어서 자른 선만 기준으로 차이를 비교해버렸다!
verti.append(int(paper[0]))

# 가로 범위를 정렬해서 가장 차이가 큰 거 찾고
def largestarea(lst):
    lst.sort()
    maxlength = 0
    for idx in range(1, len(lst)):
        if lst[idx] - lst[idx-1] > maxlength:
            maxlength = lst[idx] - lst[idx-1]
    return maxlength            
# 같은 로직으로 세로 범위도 정렬해서 가장 차이가 큰 거 찾기

print(largestarea(hori[:]) * largestarea(verti[:]))

"""
시작점과 끝점도 포함시켜야 제대로 된 종이 사각형의 넓이를 구할 수 있는데,
생각은 그렇게 해놓고 코드를 짤 때는 종이를 자른 것 내부의 범위만 구할 수 있게 해서
답이 0이 나왔다.
"""
# visual studio는 실행시 ctrl + f5
