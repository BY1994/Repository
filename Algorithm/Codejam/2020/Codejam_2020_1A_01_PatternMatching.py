"""
Wrong Answer: Case #1: 표시 안 붙임
Runtime Error: f string 사용 불가
"""
for testcase in range(1, int(input())+1):
    word = '*'
    isitpossible = True
    for numofword in range(int(input())):
        inputword = input()
        leninput = len(inputword)
        lenword = len(word)
        if isitpossible == False:
            continue
        for i in range(-1, -101, -1):
            # 뒤에서부터 오는데 inputword 길이가 끝나면 그냥 나가면 되고
            # word의 길이가 끝나면 inputword를 더 이어 붙어야함 (inputword로 대체)
            if leninput < -i:
                break
            elif lenword < -i:
                word = inputword
                break
            if inputword[i] != word[i] and word[i] != '*' and inputword[i] != '*':
                isitpossible =  False
                break

    if isitpossible == False:
        print('Case #%d: ' % (testcase)+'*')
    elif leninput == 1:
        print('Case #%d: A' % (testcase))
    else:
        print('Case #%d: ' % (testcase)+word[1:])
        

        
