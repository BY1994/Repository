'''
Round 1A Hacked Exam
=> WA

Sample Input)
4
1 3
FFT 3
1 3
FFT 2
2 6
FFTTTF 2
FTFTFT 4
2 2
FF 1
TT 1

Sample Output)
Case #1: FFT 3/1
Case #2: FFT 2/1
Case #3: FTFFFT 4/1
Case #4: TF 1/1

'''

T = int(input())
for testcase in range(T):
    maxscore = 0
    answer = ""
    N, Q = map(int, input().split())
    for n in range(N):
        input_data, score = input().split()
        if int(score) >= maxscore:
            maxscore = int(score)
            answer = input_data
    print(f"Case #{testcase+1}: {answer} {maxscore}/1")
