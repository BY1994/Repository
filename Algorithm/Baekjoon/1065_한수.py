""" 
백준 알고리즘 1065
백준 Online Judge - 문제 - 단계별로 풀어보기 - 함수 사용하기 - 한수

문제)
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력)
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
110

출력)
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
99

최초 작성 2019.01.23 PBY
"""

# input
N = int(input()) 
count = 0
for n in range(1, N+1):
        if len(str(n)) == 1:
                count += 1
        else:
                pre = str(n)[1]
                seq = int(str(n)[1]) - int(str(n)[0])
                for i in str(n)[2:]:
                        if (int(i) - int(pre)) != seq:
                                break
                        pre = i
                else:
                        count += 1
print(count)

# visual studio는 실행시 ctrl + f5