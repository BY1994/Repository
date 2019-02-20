# tensorflow 패키지 불러오기
import tensorflow as tf

# 문자열을 하나의 상수로 정의 (파이썬 할당과는 다르다)
hello = tf.constant('Hello, Tensorflow!')

# 연산 그래프 초기화를 위해 세션을 생성
session = tf.Session()

# 그래프가 실행되고 특정 변수를 반환
print(session.run(hello))
