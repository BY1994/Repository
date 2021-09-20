"""
2845 파티가 끝나고 난 뒤

" ".join(list) 형식은 내부 인자가 string이어야한다.
* 을 붙이면 print() 함수 내부에 여러 개의 인자를 넘겨준 효과가 난다.
https://www.daleseo.com/python-lists-print/
"""

L, P = map(int, input().split())
news = list(map(int, input().split()))
print(*list(map(lambda x: x - (L*P), news)), sep = " ")
