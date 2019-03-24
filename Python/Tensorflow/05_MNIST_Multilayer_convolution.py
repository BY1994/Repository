"""
텐서플로 레이어 API에서 제공하는 메소드 이용
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist_data = input_data.read_data_sets('MNIST_data', one_hot = True)

input_size = 784
no_classes = 10
batch_size = 100
total_batches = 200

x_input = tf.placeholder(tf.float32, shape=[None, input_size])
y_input = tf.placeholder(tf.float32, shape=[None, no_classes])

# 텐서보드를 사용해 훈련 프로세스를 시각화
# 변수의 통계를 시각화하려면 tf.summary에 변수의 통계값이 추가되어야한다.
def add_variable_summary(tf_variable, summary_name):
    with tf.name_scope(summary_name + '_summary'):
        mean = tf.reduce_mean(tf_variable)
        tf.summary.scalar('Mean', mean)
        with tf.name_scope('standard_deviation'):
            standard_deviation = tf.sqrt(tf.reduce_mean(
                tf.square(tf_variable - mean)))
        tf.summary.scalar('StandardDeviation', standard_deviation)
        tf.summary.scalar('Maximum', tf.reduce_max(tf_variable))
        tf.summary.scalar('Minimum', tf.reduce_min(tf_variable))
        tf.summary.histogram('Histogram', tf_variable)


# 이전 모델과 달리 MNIST 데이터를 정사각형 형태로 크기를 변경하고 2차원 이미지 형태로 사용
# 이미지를 28 x 28 이미지 픽셀 크기로 변형
x_input_reshape = tf.reshape(x_input, [-1, 28, 28, 1],
                             name = 'input_reshape')
# => 차원값이 -1이라는 것은 배치 크기가 임의의 수가 될 수 있음을 의미
# => name은 텐서보드 그래프에 반영돼 쉽게 이해할 수 있음

# 입력, 필터, 커널, 활성화가 정의된 2D 컨볼루션 레이어 정의
def convolution_layer(input_layer, filters, kernel_size = [3, 3],
                      activation = tf.nn.relu):
    layer = tf.layers.conv2d(
        inputs = input_layer,
        filters = filters,
        kernel_size = kernel_size,
        activation = activation,
    )
    add_variable_summary(layer, 'convolution')
    return layer
# => kernel_size와 activation에 대한 디폴트 값을 줌
# => 요약 데이터는 레이어에 추가되고, 해당 레이어는 반환됨
# => 함수를 호출할 때마다 input_layer가 매개변수로 주입되어야함

# 풀링 레이어에 대한 함수
def pooling_layer(input_layer, pool_size = [2,2], strides = 2):
    layer = tf.layers.max_pooling2d(
        inputs = input_layer,
        pool_size = pool_size,
        strides = strides
    )
    add_variable_summary(layer,'pooling')
    return layer
# => pool_size와 strides 디폴트 값이 주어지지만 필요한 경우 변경 가능
# => 마찬가지로 레이어에 요약 데이터 추가됨

# 밀집 레이어 정의
def dense_layer(input_layer, units, activation=tf.nn.relu):
    layer = tf.layers.dense(
        inputs = input_layer,
        units = units,
        activation = activation
    )
    add_variable_summary(layer, 'dense')
    return layer
# => activation에 대한 기본값을 갖고 있으며, 변수 요약 데이터 추가

# 레이어들은 그래프로 연결되었으며, 아직 초기화되기 전이다.
# 첫번째 컨볼루션 레이어에서 샘플링된 특성을 더 나은 특성으로 변환하기 위해
# 새로운 컨볼루션 레이어 추가 가능
convolution_layer_1 = convolution_layer(x_input_reshape, 64)
pooling_layer_1 = pooling_layer(convolution_layer_1)
convolution_layer_2 = convolution_layer(pooling_layer_1, 128)
pooling_layer_2 = pooling_layer(convolution_layer_2)
flattened_pool = tf.reshape(pooling_layer_2, [-1, 5*5*128],
                            name='flattened_pool')
dense_layer_bottleneck = dense_layer(flattened_pool, 1024)
# => 컨볼루션 레이어 간의 유일한 차이점은 필터 크기
# => 커널과 스트라이드 매개변수 값을 선택하는 것은 임의이며 경험에 의해 선택
# => 밀집 레이어 API는 단일 차원의 벡터를 특정 개수의 숨겨진 유닛(1024개)에 매핑시킨다.
# => 숨겨진 레이어는 ReLU 활성화 함수로 이어져 비선형 연산이 되다.

# 드롭아웃 확률을 가진 드롭아웃 레이어
# 훈련 모드는 드롭아웃 적용 여부에 따라 True 또는 False로 설정할 수 있으며, 훈련을 위해
# True로 설정한다. 하지만 정확도 계산시 해당 값이 변경되어야해서 부울 값을 저장해둔다.
dropout_bool = tf.placeholder(tf.bool)
dropout_layer = tf.layers.dropout(
    inputs = dense_layer_bottleneck,
    rate = 0.4,
    training = dropout_bool
)

# 드롭아웃 레이어를 로짓이라는 밀집 레이어에 주입
# 로짓은 클래스 개수로 이어지는 활성화 함수를 가진 마지막 레이어
logits = dense_layer(dropout_layer, no_classes)

# 이전처럼 로짓이 소프트맥스 레이어를 통과한 후 교차 엔트로피 계산을 수행
# 텐서보드의 좀 더 나은 시각화를 위해 이름 범주에 추가
with tf.name_scope('loss'):
    softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
        labels=y_input, logits=logits)
    loss_operation = tf.reduce_mean(softmax_cross_entropy, name='loss')
    tf.summary.scalar('loss', loss_operation)

# 손실 함수를 tf.train API의 메소드를 이용해 최적화
with tf.name_scope('optimiser'):
    optimiser = tf.train.AdamOptimizer().minimize(loss_operation)

# 정확한 예측값과 정확도 계산을 위해 이름 범주를 추가
# 정확도에 대한 스칼라 요약 데이터도 추가
with tf.name_scope('accuray'):
    with tf.name_scope('correct_prediction'):
        predictions = tf.argmax(logits, 1)
        correct_predictions = tf.equal(predictions, tf.argmax(y_input, 1))
    with tf.name_scope('accuracy'):
        accuracy_operation = tf.reduce_mean(
            tf.cast(correct_predictions, tf.float32))
    tf.summary.scalar('accuracy', accuracy_operation)

# 세션을 시작하고 변수를 초기화
session = tf.Session()
session.run(tf.global_variables_initializer())

# 요약 데이터를 모두 합쳐야하며, 훈련 요약 데이터와 테스팅 요약 데이터를 작성
# 하기 위한 파일도 정의
merged_summary_operation = tf.summary.merge_all()
train_summary_writer = tf.summary.FileWriter('/tmp/train', session.graph)
test_summary_writer = tf.summary.FileWriter('/tmp/test')

# 배치에서 데이터가 로드되고 훈련을 시작
test_images, test_labels = mnist_data.test.images, mnist_data.test.labels

for batch_no in range(total_batches):
    mnist_batch = mnist_data.train.next_batch(batch_size)
    train_images, train_labels = mnist_batch[0], mnist_batch[1]
    _, merged_summary = session.run([optimiser, merged_summary_operation],
                                    feed_dict={
                                        x_input: train_images,
                                        y_input: train_labels,
                                        dropout_bool: True
                                        })
    train_summary_writer.add_summary(merged_summary, batch_no)
    if batch_no % 10 == 0:
        merged_summary, _ = session.run([merged_summary_operation,
                                         accuracy_operation], feed_dict={
                                             x_input: test_images,
                                             y_input: test_labels,
                                             dropout_bool: False
                                             })
        test_summary_writer.add_summary(merged_summary, batch_no)
