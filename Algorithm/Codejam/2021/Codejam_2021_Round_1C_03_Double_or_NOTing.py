"""
Codejam 2021 1C
# 03

시간 안에 작성 못함

"""

def my_str(input_str):
    return int("0b"+input_str,2)

T = int(input())
for testcase in range (T):
    answer = 0
    # 이진수로 변환
    start, end = input().split()
    start2 = my_str(start)
    end2 = my_str(end)
    #start2, end2 = map(my_str, input().split())
    # end에 있는 모양을 하나씩 왼쪽으로 보내면서 최대한 같은 패턴 오버랩 찾기
    # 둘이 xor 해서 완전히 다르거나
    # 둘이 빼서 0이 나오거나...?
    # - 오버랩 못찾으면 IMPOSSIBLE 출력
    for i in range(len(end)):
        # start의 [끝 부분] 이랑 end 의 [시작 부분] 같은지 확인

    # 오버랩 찾으면 뒤에 0을 붙여서 늘림
    # 1로 끝나면 한 번 뒤집어주고 필요한 만큼 0 붙임
    # 그리고 정답이 나올 때까지 변환한 횟수 계산
    print(f"Case #{testcase+1}: {answer}")
