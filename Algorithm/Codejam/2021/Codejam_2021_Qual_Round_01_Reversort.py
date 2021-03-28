'''
2021 Codejam Qualification Round
01_Reversort

※ distinct integers

Sample Input
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1

Sample Output
Case #1: 6
Case #2: 1
Case #3: 12
'''

T = int(input())
for t in range(T):
    answer = 0
    N = int(input())
    input_list = list(map(int, input().split()))
    for i in range(N-1):
        min_index = input_list.index(min(input_list[i:]))
        answer += min_index - i + 1
        input_list[i:min_index+1] = reversed(input_list[i:min_index+1])
    print(f"Case #{t+1}: {answer}")


'''
1. 문제 이해 잘못
i 부터 j 까지 reverse해야하는데
선택정렬처럼 구현함

T = int(input())
for t in range(T):
    answer = 0
    N = int(input())
    input_list = list(map(int, input().split()))
    for i in range(N-1):
        min_index = input_list.index(min(input_list[i:]))
        answer += min_index - i + 1
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    print(f"Case #{t+1}: {answer}")
'''
