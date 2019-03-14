""" 
2447
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N이 주어진다. N은 항상 3의 제곱꼴인 수이다. (1, 3, 9, 27, ...) (N=3k, 0 ≤ k < 8)

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.

최초작성 2019.03.14 PBY
"""

def startpattern(pattern, depth):
    if depth == N:
        print(pattern)
    else:
        patternlist = pattern.split('\n')
        # 위에 상단바
        result1 = ''
        result2 = ''
        for i in range(len(patternlist)):
            result1 += patternlist[i] * 3 + '\n'
            result2 += patternlist[i] + ' '*(depth) + patternlist[i] + '\n' # 여기를 depth가 아닌 N//3으로 잘못 생각했다.
        startpattern(result1 + result2 + result1[:-1], depth*3) # [:-1]을 해서 for문 때문에 마지막에 붙은 \n을 없애주었다.
        
N = int(input())
pattern = '*'
if N == 1:
    print(pattern)
else:
    startpattern(pattern, 1)

        
# visual studio는 실행시 ctrl + f5
