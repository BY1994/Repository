""" 
백준 알고리즘 2108
백준 Online Judge - 문제 - 단계별로 풀어보기 - 정렬해보기 - 통계학

문제)
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력)
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

최초 작성 2019.02.27 PBY
"""

num = int(input())
numbers = []

for _ in range(num):
    numbers.append(int(input()))

# 산술평균
average = sum(numbers)/len(numbers)

# 반올림
straverage = str(average)
for idx in range(len(straverage)-1):
    if straverage[idx] == '.':
        if straverage[idx+1] >= '5': # 아스키코드값
            average = int(straverage[:idx]) # 0 전까지 자름
            average += 1
        else:
            average = int(straverage[:idx])
print(average)
        
# 중앙값
sortednumbers = sorted(numbers)
print(sortednumbers[len(numbers)//2])

# 최빈값
cnt = {}
for n in numbers:
    if n not in cnt:
        cnt[n] = 1
    else:
        cnt[n] += 1
print('cnt',cnt)

# 최빈값 구현        
#cnt = [0] *  # 이건 5 크기만큼 만들어지는데,
#for n in numbers:
#    cnt[n-1] += 1

# 제일 큰 값
max_ind_value = [0, 0]
for n in cnt:
    if max_ind_value[1] < cnt[n]:
        max_ind_value[0] = n
        max_ind_value[1] = cnt[n] 

# 그 중 숫자가 제일 작은 값
for n in cnt:
    if max_ind_value[1] == cnt[n] and max_ind_value[0] > n:
        max_ind_value[0] = n
        max_ind_value[1] = cnt[n] 
print(max_ind_value[0])

# 그 숫자보다 하나 큰 값


# 범위
print(max(numbers)-min(numbers))

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
