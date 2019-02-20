# tensorflow 패키지 불러오기
import tensorflow as tf

# placeholder 정의
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 합 연산을 정의 (정의만 하고 실행되지는 않는다)
z = x + y

# 세션을 생성해서 연산을 수행할 준비를 한다
session = tf.Session()

# 딕셔너리 포맷으로 플레이스홀더의 값을 정의
values = {x: 5.0, y: 4.0}

# 변수 z와 값을 이용해 세션을 실행
result = session.run([z], values)
print(result)
