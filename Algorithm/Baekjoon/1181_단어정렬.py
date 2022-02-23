"""
1181 단어 정렬
"""

N = int(input())
words = set()
for i in range(N):
    word = input()
    words.add((len(word), word))

words = sorted(words, key = lambda x:(x[0], x[1]))

for word in words:
    print(word[1])

# https://www.acmicpc.net/source/15521950
"""
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))
"""
