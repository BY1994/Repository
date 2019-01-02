# Python  기초
파이썬 기초 문법

##  I. 입출력
### (1) 입력
파이썬에서 입력 받기

- `input()` :
사용자의 입력을 받는 함수
```python
n = input()
```
- `sys.stdin`:
표준 입력을 받는 함수
```python
import sys

for i in sys.stdin:
    print(i, end="")
```

### (2)  출력
파이썬에서 출력 하기

- `print()`:
인자를 출력하는 함수
```python
print("Hellow World")
print("""
여러줄
출력하는
방법
""")
```