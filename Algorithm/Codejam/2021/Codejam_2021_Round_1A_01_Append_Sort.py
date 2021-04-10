'''
Round 1A Append Sort

=> Test Set 1 Success & Test Set 2 Fail (WA)

Sample Input)
4
3
100 7 10
2
10 10
3
4 19 1
3
1 2 3

Sample Output)
Case #1: 4
Case #2: 1
Case #3: 2
Case #4: 0

내가 만든 반례
(1)
1
3
100 10 1
Case #1: 4 => 101, 123 이런 식으로 답은 3이어야 한다
앞 숫자랑 무조건 같게 가다가 마지막에 0을 붙이게 한 게 잘못된 듯


답은 3인데 프린트하니까 이상한 숫자 나옴
1
3
100 10 1
['100', '101', '12']
Case #1: 3
] += input_list[i][i_1_len:-1] 이렇게 해야하는데 [i_len - i_1_len+1:-1] 이런식으로 잘라서
잘못된 거였음
이걸 틀리니까 숫자가 3개 넘어가면 틀렸을 듯

(2)
1
3
9 9 9
['9', '9', '9']
Case #1: 0

'''


T = int(input())

for testcase in range(T):
    answer = 0
    N = int(input())
    input_list = input().split()

    # input list를 돌면서 숫자를 앞부터 비교...
    # 앞 수의 길이만큼 가야함
    for i in range(N-1):
        i_len = len(input_list[i])
        i_1_len = len(input_list[i+1])
        if (int(input_list[i]) < int(input_list[i+1])):
            continue

        for c in range(i_len):
            A = int(input_list[i][c])
            # 비교할 길이가 안 되면 continue만 하다가 else로 넘어가게
            if c > len(input_list[i+1])-1:
                continue
            B = int(input_list[i+1][c])
            
            # A와 B크기 비교
            # 한번이라도 크면 그대로 0 붙이면서 가면 됨
            if (B > A):
                number_zero = i_len - len(input_list[i+1])
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                # 그대로 다음 i로 가야함
                break
            # 한번이라도 작으면 그대로 0 붙이면서 가면 됨
            elif (B < A):
                number_zero = i_len - len(input_list[i+1])+1
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                break
            # 아래 조건 다시 확인하러 가야함 else 같으면...
        else:
            # 자리수 비교해서
            # 둘이 자리수가 다르면 마지막 숫자가 9면 무조건 0 붙여서 키우고
            # 마지막 숫자가 9가 아니면 무조건 마지막 숫자만 1 크게 따라감
            # 109 10 / 109 1 / 1000 보다 110 이 되는 경우가 더 좋은거 아닌가?
            # 마지막 숫자가 9고 내가 2자리 여유가 있으면 10 으로 끝내고
            # 여유가 없으면 00 으로 끝내기 여유가 없으면 무조건 다 0으로 가야함

            # !!! 마지막 9 상관 없이 앞쪽 자리가 더 작거나 큰 경우 있음
            # 109 / 11 이면?
            if (input_list[i][-1] == "9"):
                if (i_len - len(input_list[i+1]) >= 2):
                    number_zero = i_len - len(input_list[i+1]) - 2
                    input_list[i+1] += input_list[i][i_1_len:-2] + "10"
                    answer += number_zero + 2
                 # 반례 생겨서 예외처리 추가
                else:
                    # 여유가 하나도 없는 경우 0 하나 추가해야함
                    number_zero = i_len - len(input_list[i+1])+1
                    input_list[i+1] += "0"*(number_zero)
                    answer += number_zero
                    
            else:
                # 마지막 전까지는 같고 마지막 자리수를 하나 더 늘림
                number = i_len - i_1_len
                if (number == 0): # 10, 10 의 경우... 0이 추가되어야함
                    input_list[i+1] += "0"
                    answer += 1
                else:
                    input_list[i+1] += input_list[i][i_1_len:-1] +str(int(input_list[i][-1])+1)
                    answer += number
                    
    print(input_list)
    print(f"Case #{testcase+1}: {answer}")

"""
# 반례 2
T = int(input())

for testcase in range(T):
    answer = 0
    N = int(input())
    input_list = input().split()

    # input list를 돌면서 숫자를 앞부터 비교...
    # 앞 수의 길이만큼 가야함
    for i in range(N-1):
        i_len = len(input_list[i])
        i_1_len = len(input_list[i+1])
        if (int(input_list[i]) < int(input_list[i+1])):
            continue

        for c in range(i_len):
            A = int(input_list[i][c])
            if c > len(input_list[i+1])-1:
                continue
            B = int(input_list[i+1][c])
            
            # A와 B크기 비교
            # 한번이라도 크면 그대로 0 붙이면서 가면 됨
            if (B > A):
                number_zero = i_len - len(input_list[i+1])
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                # 그대로 다음 i로 가야함
                break
            # 한번이라도 작으면 그대로 0 붙이면서 가면 됨
            elif (B < A):
                number_zero = i_len - len(input_list[i+1])+1
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                break
            # 아래 조건 다시 확인하러 가야함 else 같으면...
        else:
            # 자리수 비교해서
            # 둘이 자리수가 다르면 마지막 숫자가 9면 무조건 0 붙여서 키우고
            # 마지막 숫자가 9가 아니면 무조건 마지막 숫자만 1 크게 따라감
            # 109 10 / 109 1 / 1000 보다 110 이 되는 경우가 더 좋은거 아닌가?
            # 마지막 숫자가 9고 내가 2자리 여유가 있으면 10 으로 끝내고
            # 여유가 없으면 00 으로 끝내기 여유가 없으면 무조건 다 0으로 가야함

            # !!! 마지막 9 상관 없이 앞쪽 자리가 더 작거나 큰 경우 있음
            # 109 / 11 이면?
            if (input_list[i][-1] == "9"):
                if (i_len - len(input_list[i+1]) >= 2):
                    number_zero = i_len - len(input_list[i+1]) - 2
                    input_list[i+1] += input_list[i][i_1_len:-2] + "10"
                    answer += number_zero + 2
                elif (i_len - len(input_list[i+1]) >= 1):
                    number_zero = i_len - len(input_list[i+1])+1
                    input_list[i+1] += "0"*(number_zero)
                    answer += number_zero                    
            else:
                # 마지막 전까지는 같고 마지막 자리수를 하나 더 늘림
                number = i_len - i_1_len
                if (number == 0): # 10, 10 의 경우... 0이 추가되어야함
                    input_list[i+1] += "0"
                    answer += 1
                else:
                    input_list[i+1] += input_list[i][i_1_len:-1] +str(int(input_list[i][-1])+1)
                    answer += number
                    
    print(input_list)
    print(f"Case #{testcase+1}: {answer}")
"""

"""
# 반례 1 : 앞 숫자랑 무조건 같게 가다가 마지막에 0을 붙이게 한 게 잘못된 듯

T = int(input())

for testcase in range(T):
    answer = 0
    N = int(input())
    input_list = input().split()

    # input list를 돌면서 숫자를 앞부터 비교...
    # 앞 수의 길이만큼 가야함
    for i in range(N-1):
        i_len = len(input_list[i])
        
        for j in range(i_len):
            # 앞 숫자의 가장 큰 자리수부터
            A = int(input_list[i][j])
            # 뒷 숫자가 자리수가 되는지 확인
            if (len(input_list[i+1]) < i_len):
                # 자리수 안 되면 앞 숫자랑 똑같은 수 붙이면서 따라감
                B = A
                input_list[i+1] += str(A)
                answer += 1
            else:
                B = int(input_list[i+1][j])

            # A와 B크기 비교
            # 한번이라도 크면 그대로 0 붙이면서 가면 됨
            if (B > A):
                number_zero = i_len - len(input_list[i+1])
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                break
            # 한번이라도 작으면 그대로 0 붙이면서 가면 됨
            elif (B < A):
                number_zero = i_len - len(input_list[i+1])+1
                input_list[i+1] += "0"*(number_zero)
                answer += number_zero
                break

        # 다 돌고 나왔는데 숫자가 같은 경우
        if (input_list[i] == input_list[i+1]):
            input_list[i+1] += "0"
            answer += 1
            
    
    print(f"Case #{testcase+1}: {answer}")
"""
