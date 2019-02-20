# tensorflow 패키지 불러오기
import tensorflow as tf

# placeholder 및 연산 정의 (★ name 필수)
x = tf.placeholder(tf.float32, name='x')
y = tf.placeholder(tf.float32, name='y')
z = tf.add(x, y, name='sum')

# 세션을 생성
session = tf.Session()

# 특정 폴더에 그래프를 저장
summary_writer = tf.summary.FileWriter('/tmp/1', session.graph)
