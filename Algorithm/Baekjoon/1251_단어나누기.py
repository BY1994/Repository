"""
1251 단어 나누기

브루트포스, 정렬
"""
word = input()
n = len(word)
reversed_word = word[:2] + word[2:][::-1]
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = word[:i+1][::-1] + word[i+1:j+1][::-1] + word[j+1:][::-1]
            if reversed_word > temp:
                reversed_word = temp
print(reversed_word)
