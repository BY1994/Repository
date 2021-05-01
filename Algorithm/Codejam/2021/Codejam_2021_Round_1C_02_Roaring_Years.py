"""
Codejam 2021 1C
# 02

Sample만 Pass

아래 반례 Case도 Pass
1이 들어오면? 12 가나오도록?
99 넣으면 910 나오네...
=> 이런 경우에 다 123.. 이렇게 나오도록
초기 answer 값을 다시 세팅해야할 듯
1 부터 n 까지 되도록 변경함

"""

T = int(input())
for testcase in range (T):
    number = input()
    length = len(number)
    answer = ""
    answer_len = 0
    answer_init = "1"
    while (answer_len < length+1):
        answer += answer_init
        answer_len += len(answer_init)
        answer_init = str(int(answer_init)+1)

    for cur_len in range(1,length//2 + 1):
        # 앞에서 cur_len 만큼 잘라서....
        # 10 의 배수가 된 경우에는 cur_len+1이 됨...
        # 그냥 앞에거를 자르고 +1 했을 때의 내거의 크기를 다시 재면 됨
        flag = 0
        my = int(number[:cur_len])
        my_len = 0
        temp_answer = ""
        for i in range(length//cur_len + 1):
            # 불가능하면 맨 앞에 와서 숫자 하나 더 하고 한 번 더 반복함
            # 그래도 불가능하면 끝
            # 가능하면 무조건 answer 업데이트
            str_my = str(my)
            temp_answer += str_my
            my_len += len(str_my)
            
            if (my_len == length):
                # 이전 숫자 보다 커야함
                if int(number) < int(temp_answer):
                    flag = 1
                    answer = temp_answer
                break
            elif (my_len > length):
                if (int(answer) > int(temp_answer)):
                    answer = temp_answer
                break
            
            my = my+1
            # 정확히 그 숫자가 나오면 나가고 flag = 1
            # 기존 개수를 넘어버리면 그냥 나감
        
        my = int(number[:cur_len]) + 1
        my_len = 0
        temp_answer = ""
        if (flag == 1): continue
        for i in range(length//cur_len + 1):
            str_my = str(my)
            temp_answer += str_my
            my_len += len(str_my)
            
            if (my_len == length):
                # 이전 숫자 보다 커야함
                if int(number) < int(temp_answer):
                    flag = 1
                    answer = temp_answer
                break
            elif (my_len > length):
                if (int(answer) > int(temp_answer)):
                    answer = temp_answer
                break
            
            my = my+1
            
            
    print(f"Case #{testcase+1}: {answer}")
