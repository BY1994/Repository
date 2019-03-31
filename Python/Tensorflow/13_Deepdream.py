"""
Deep Dream

2019.03.27 PBY 최초작성
2019.03.31 PBY 주석추가

컴퓨터 비전과 딥러닝 p. 120
"뉴런 활성화는 이미지를 합성하는 대신 네트워크의 일부 레이어에서 증폭되기도 한다.
특징의 영향을 보기 위해 원본 이미지를 증폭하는 개념을 DeepDream이라 한다."
"""

print('import settings')
import os
import numpy as np
import PIL.Image
import urllib.request
from tensorflow.python.platform import gfile
import zipfile
import tensorflow as tf

# ImageNet 데이터셋으로 사전 훈련된 인셉션 모델 파일은 구글에서 제공한다.
# 여기서는 제공되는 모델을 다운로드해 예제에 활용한다.
# 다음과 같이 ZIP으로 압축된 모델 파일을 다운로드한 후 폴더에 압축 해제한다.
# => zip 파일 다운 코드가 실행이 잘 안 돼서, 직접 링크로 접속해서 다운 받아 압축해제했다...
print('set paths and zipfile')
work_dir = 'C:/Users/BY/Downloads/'
"""
model_url = 'https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip'
file_name = model_url.split('/')[-1]

file_path = os.path.join(work_dir, file_name)

if not os.path.exists(file_path):
    file_path, _ = urllib.request.urlretrieve(model_url, file_path)

zip_handle = zipfile.ZipFile(file_path, 'r') # zipfile.BadZipFile: File is not a zip file
zip_handle.extractall(work_dir)
zip_handle.close()
"""

# 세션을 통해 훈련된 모델을 불러온 후 사용한다.
# 그래프를 초기화하고, 다운로드된 모델의 그래프 정의를 메모리에 적재한다. 
print('tensorflow graph')
graph = tf.Graph()
session = tf.InteractiveSession(graph=graph)
model_path = os.path.join(work_dir, 'tensorflow_inception_graph.pb')
with gfile.FastGFile(model_path, 'rb') as f:
    graph_defnition = tf.GraphDef()
    graph_defnition.ParseFromString(f.read())

# 전처리 단계에서는 입력에서 ImageNet 평균을 빼준다.
# 전처리된 이미지는 그래프의 입력으로 사용된다. 
input_placeholder = tf.placeholder(np.float32, name='input')
imagenet_mean_value = 117.0
preprocessed_input = tf.expand_dims(input_placeholder-imagenet_mean_value, 0)
tf.import_graph_def(graph_defnition, {'input': preprocessed_input})


# 이중 선형 보간을 위해 resize_image 함수가 필요하다.
# 텐서플로 세션에 이미지 크기를 조정하는 resize 함수 메소드를 추가한다.
print('resize_image')
def resize_image(image, size):
    resize_placeholder = tf.placeholder(tf.float32)
    resize_placeholder_expanded = tf.expand_dims(resize_placeholder, 0)
    resized_image = tf.image.resize_bilinear(
        resize_placeholder_expanded,
        size
    )[0, :, :, :]
    return session.run(resized_image, feed_dict={resize_placeholder: image})


# 작업 디렉터리의 이미지를 메모리에 적재하고 부동 소수점 값으로 변환한다.
image_name = 'C:/Users/BY/Downloads/bada.jpg'
image = PIL.Image.open(image_name)
image = np.float32(image)

# 옥타브 수, 크기, 스케일 공간의 스케일은 다음과 같이 정의된다.
# 여기 값은 해당 예제에서 잘 동작하기 때문에 다른 이미지를 사용한다면 크기에 따라
# 조정이 필요하다. 
no_octave = 4
scale = 1.4
window_size = 50 #314 # 이미지의 배수

# DeepDream을 위해 레이어를 선택한다.
# 다음과 같이 해당 레이어의 평균은 objective 함수가 된다. (교재에 objective 함수 부분이 생략)
# 최적화를 위해 이미지의 경사를 계산한다.
print("cal gradient")
layer = 'mixed4d_3x3_bottleneck_pre_relu'
channel = 139 # 65 특징을 잡는 거의 개수
objective_fn = graph.get_tensor_by_name("import/%s:0"%layer)[:,:,:,channel]
score = tf.reduce_mean(objective_fn) # objective_fn 함수가 없다!
gradients = tf.gradients(score, input_placeholder)[0]

# 다양한 스케일로 크기를 조절한 옥타브 이미지로 차이를 계산
octave_images = []
for i in range(no_octave-1):
    image_height_width = image.shape[:2]
    scaled_image = resize_image(
        image, np.int32(np.float32(image_height_width) / scale)
    )
    image_difference = image - resize_image(scaled_image, image_height_width)
    image = scaled_image
    octave_images.append(image_difference)

# 모든 옥타브 이미지를 사용해 최적화를 실행
# 윈도우가 이미지를 지나가면서 DeepDream 이미지를 생성하기 위한 경사 활성화를 계산한다.
for octave_idx in range(no_octave):
    if octave_idx > 0:
        image_difference = octave_images[-octave_idx]
        image = resize_image(image, image_difference.shape[:2]) + image_difference

    for i in range(10):
        image_height, image_width = image.shape[:2]
        sx, sy = np.random.randint(window_size, size=2)
        shifted_image = np.roll(np.roll(image, sx, 1), sy, 0)
        gradient_values = np.zeros_like(image)

        for y in range(0, max(image_height - window_size // 2, window_size), window_size):
            for x in range(0, max(image_width - window_size // 2, window_size), window_size):
                sub = shifted_image[y:y+window_size, x:x+window_size]
                gradient_windows = session.run(gradients, {input_placeholder: sub})
                gradient_values[y:y+window_size, x:x+window_size] = gradient_windows
                gradient_windows = np.roll(np.roll(gradient_values, -sx, 1), -sy, 0)
                image += gradient_windows*(1.5/(np.abs(gradient_windows).mean() + 1e-7))

# DeepDream을 생성하기 위한 최적화가 완료됐다. 다음과 같이 값을 클리핑해 저장한다.
image /= 255.0
image = np.uint8(np.clip(image, 0, 1)*255)
print("save files")
PIL.Image.fromarray(image).save(work_dir+'dream2.jpg', 'jpeg')
    
