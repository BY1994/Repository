"""
백준 5430 AC

2019-03-18 PBY최초작성
"""

T = int(input())
for _ in range(T):
    operation = input()
    size = int(input())
    array = input() # [ 1 , 2 , 3
    front = 0
    end = size-1
    direct = 1
    """
        if len(array) == 2: # [ ]
            print('error')
        else:
    """
    # 명령어를 돌면서
    for o in operation:
        if o == "R":
            if direct == 1:
                direct = 2
            elif direct == 2:
                direct = 1 # R작업은 조건 상관없이 무조건 수행 D를 해야만 요소가 하나씩 줄고 변화가 생기니까
        else: # "D"
            if direct == 1:
                front += 1
            elif direct == 2:
                end -= 1
            # 배열에 아무것도 안 남았으면 끝
            if front > end+1: # 반례 - [] 빈 거를 한 번 더 호출해야?
                ans = False
                break
    else:
        ans = True
            
    if ans == True:
        # 배열에 두 자리 숫자가 있어도 못 찾는다.
        array = array[1:-1].split(',')
        if direct == 1:
            print('['+','.join(array[front:end+1])+']')
        else:
            print('['+','.join(array[front:end+1][::-1])+']')
    else:
        print('error')

"""
틀렸습니다 - 예외 front >= end로 쓰면 안되고 front > end로 써야함
1
DR
2
[1,1]

틀렸습니다 - 텍스트로 slicing해서 문제
지금 내 코드는 배열에 두 자리 숫자가 안 들어간다!!!!!!

틀렸습니다
[]은 R을 수행할 수 있다. (https://www.acmicpc.net/board/view/10073)
1
R
0
[]

틀렸습니다.
질문 답변 정리본
https://www.acmicpc.net/board/view/25456
=> 여기에는 없었는데 내 코드는 굉장히 기본적인 것이 문제였다.
1
DD
2
[100,99]
DD를 두 번 쓰면 []를 출력하면 되는데, 이게 error인줄 알고 error를 출력하였다.
"""
