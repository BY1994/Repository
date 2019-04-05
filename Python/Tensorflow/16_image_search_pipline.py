"""
검색 파이프라인 구축

2019.04.03 PBY 최초작성
컴퓨터 비전과 딥러닝
"""

# 필요한 라이브러리 로드
import os
import urllib.request
from tensorflow.python.platform import gfile
import tarfile
import tensorflow as tf
import numpy as np

# 그래프의 정의와 가중치를 포함한 사전 훈련된 모델을 다운로드
print("======load settings======")
work_dir = 'C:/Users/BY/Downloads' # 필요한 작업 폴더 직접 정의
model_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
file_name = model_url.split('/')[-1]
file_path = os.path.join(work_dir, file_name)

# 다운로드한 모델을 로컬 폴더에 압축 해제
if not os.path.exists(file_path):
    file_path, _ = urllib.request.urlretrieve(model_url, file_path)
tarfile.open(file_path, 'r:gz').extractall(work_dir)

# 그래프는 프로토콜 버퍼 (protobuf) 형식으로 파일에 저장된다.
# 이 형식을 문자열로 읽어들여 tf.Graphdef() 객체에 전달하고 메모리로 가져온다.
model_path = os.path.join(work_dir, 'classify_image_graph_def.pb')

with gfile.FastGFile(model_path, 'rb') as f:
    graph_definition = tf.GraphDef()
    graph_definition.ParseFromString(f.read())

# 인셉션 모델에서 병목 레이어명은 pool_3/_reshape:0이고 2048차원이다.
# 플레이스홀더명은 DecodeJpeg/contents:0이고 크기 조절 텐서명은 ResizeBilinear:0이다.
# 그래프 정의를 이후의 작업을 위해 요구되는 반환 텐서와 tf.import_graph_def로 가져올 수 있다.
print("=====extract bottleneck======")
bottleneck, image, resized_input = (
    tf.import_graph_def(
        graph_definition,
        name='',
        return_elements=['pool_3/_reshape:0',
                         'DecodeJpeg/contents:0',
                         'ResizeBilinear:0']
    )
)

# 쿼리와 대상 이미지를 가져와서 메모리에 적재한다.
# gfile 함수를 사용해 이미지를 메모리에 빠르게 적재할 수 있다.
query_image_path = os.path.join(work_dir, 'cat.1000.jpg') # dogs-vs-cats 예시에서 가져온 사진
query_image = gfile.FastGFile(query_image_path, 'rb').read()
target_image_path = os.path.join(work_dir, 'cat.1001.jpg')
target_image = gfile.FastGFile(target_image_path, 'rb').read()

# session과 이미지를 사용해 이미지로부터 병목 특징을 추출하는 함수를 정의한다.
def get_bottleneck_data(session, image_data):
    bottleneck_data = session.run(bottleneck, {image:image_data})
    bottleneck_data = np.squeeze(bottleneck_data)
    return bottleneck_data

# 사전 훈련된 모델에서 병목 값을 얻기 위해 세션을 초기화하고 이미지를 전달해 추론을 진행한다.
print("=======start session=======")
session = tf.Session() # p.66
session.run(tf.global_variables_initializer())
query_feature = get_bottleneck_data(session, query_image)
print(query_feature)
target_feature = get_bottleneck_data(session, target_image)
print(target_feature)

# 쿼리 이미지와 대상 데이터베이스 간의 유사도 계산
dist = np.linalg.norm(np.asarray(query_feature) - np.asarray(target_feature))
print(dist)
