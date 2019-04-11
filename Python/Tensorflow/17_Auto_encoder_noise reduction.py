"""
자동 인코더를 사용한 노이즈 제거

2019.04.10 PBY 최초작성
참고문헌: 컴퓨터 비전과 딥러닝 p.142 ~ p.144
"""

# 필요한 라이브러리 가져오기
print("--loading packages--")
import tensorflow as tf
import numpy as np

# MNIST 데이터 로드
print("--loading data--")
from tensorflow.examples.tutorials.mnist import input_data # p. 63
mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)

# 플레이스 홀더 정의
input_size = 784 # p.64
no_classes = 10
batch_size = 100
total_batches = 200

# x_input과 y_input은 모두 자동 인코더에서와 같은 shape를 갖는다.
x_input = tf.placeholder(tf.float32, shape=[None, input_size])
y_input = tf.placeholder(tf.float32, shape=[None, input_size])

# 텐서보드용 함수 정의
print("--define functions--")
def add_variable_summary(tf_variable, summary_name): # p.68
    with tf.name_scope(summary_name + '_summary'):
        mean = tf.reduce_mean(tf_variable)
        tf.summary.scalar('Mean', mean)
        with tf.name_scope('standard_deviation'):
            standard_deviation = tf.sqrt(tf.reduce_mean(
                tf.square(tf_variable - mean)
            ))
        tf.summary.scalar('StandardDeviation', standard_deviation)
        tf.summary.scalar('Maximum', tf.reduce_max(tf_variable))
        tf.summary.scalar('Minimum', tf.reduce_min(tf_variable))
        tf.summary.histogram('Histogram', tf_variable)

# 기본 활성화로 tanh 활성화 함수를 설정해 dense_layer를 다음과 같이 정의한다.
def dense_layer(input_layer, units, activation=tf.nn.tanh):
    layer = tf.layers.dense(
        inputs=input_layer,
        units=units,
        activation=activation
    )
    add_variable_summary(layer, 'dense')
    return layer


# 자동 인코더 레이어를 정의한다.
# 이 자동 인코더는 완전 연결 레이어만 포함한다.
# 인코더 부분에는 차원을 축소시키는 세 개의 레이어가 있고,
# 디코더 부분에는 차원을 확대시키는 세 개의 레이어가 있다.
# (숨겨진 레이어의 크기는 임의로 선택한다)
layer_1 = dense_layer(x_input, 500)
layer_2 = dense_layer(layer_1, 250)
layer_3 = dense_layer(layer_2, 50)
layer_4 = dense_layer(layer_3, 250)
layer_5 = dense_layer(layer_4, 500)
layer_6 = dense_layer(layer_5, 784)

# loss와 optimise를 정의한다
# 소프트맥스 대신 시그모이드를 사용해 분류한다.
with tf.name_scope('loss'):
    softmax_cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y_input,
                                                                    logits=layer_6)
    loss_operation = tf.reduce_mean(softmax_cross_entropy, name='loss')
    tf.summary.scalar('loss', loss_operation)

with tf.name_scope('optimiser'):
    optimiser = tf.train.AdamOptimizer().minimize(loss_operation)

# 텐서보드는 다른 종류의 요약으로 image를 제공하며, 이미지 시각화에 유용하다.
# 두 개의 입력과 layer_6를 가져와서 형태를 변경하고 요약에 추가한다.
# 모든 이미지를 요약 폴더에 저장하는 것을 방지하기 위해 기본 설정으로 이미지의 수가 세 개로 제한되지만 변경가능하다.
x_input_reshaped = tf.reshape(x_input, [-1, 28, 28, 1])
tf.summary.image("noisy_images", x_input_reshaped)

y_input_reshaped = tf.reshape(y_input, [-1, 28, 28, 1])
tf.summary.image("original_images", y_input_reshaped)

layer_6_reshaped = tf.reshape(layer_6, [-1, 28, 28, 1])
tf.summary.image("reconstructed_images", layer_6_reshaped)

# 세션 정의
print("--make session--")
session = tf.Session() # p.66
session.run(tf.global_variables_initializer())

# 모든 요약이 병합되고, 요약 작성자에 그래프가 추가된다.
merged_summary_operation = tf.summary.merge_all()
train_summary_writer = tf.summary.FileWriter('/tmp/train', session.graph)

# 일반적인 임의의 노이즈를 이미지에 추가해 입력 텐서로 제공한다.
# 노이즈가 추가되면 초과되는 값들은 클리핑한다. 여기서 대상은 원본 이미지가 된다.
# 노이즈의 추가와 훈련 절차
print("--train model--")
for batch_no in range(total_batches):
    mnist_batch = mnist_data.train.next_batch(batch_size)
    train_images, _ = mnist_batch[0], mnist_batch[1]
    train_images_noise = train_images + 0.2 * np.random.normal(size=train_images.shape)
    train_images_noise = np.clip(train_images_noise, 0., 1.)
    _, merged_summary = session.run([optimiser, merged_summary_operation],
                                    feed_dict={
                                        x_input: train_images_noise,
                                        y_input: train_images,
                                    })
    train_summary_writer.add_summary(merged_summary, batch_no)

