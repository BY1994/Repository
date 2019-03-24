# 이미지 데이터 출처 kaggle.com/c/dogs-vs-cats/data
# tensorflow, pillow, SciPy
# 데이터셋 확장하기 (data augmentation) : 훈련 중 노이즈를 유발해 다양한 입력에 대해 모델이 견고해지게 만든다.
# => 이전 버전의 코드에서 generator_train 부분만 수정한다.

print("==========================")
print("====loading settings======")
import tensorflow as tf
import os
import shutil

work_dir = 'C:/Users/BY/Downloads/dogs-vs-cats/train/' #디렉토리 지정
image_names = sorted(os.listdir(os.path.join(work_dir, 'train')))

def copy_files(prefix_str, range_start, range_end, target_dir):
    image_paths = [os.path.join(work_dir, 'train', prefix_str+'.'+str(i)+'.jpg')
                   for i in range(range_start, range_end)]
    dest_dir = os.path.join(work_dir, 'data', target_dir,prefix_str)
    os.makedirs(dest_dir)
    for image_path in image_paths:
        shutil.copy(image_path, dest_dir)

"""
# 실습을 위해 고양이와 개 이미지를 1,000개만 사용
print("==========================")
print("====copy image files======")
copy_files('dog', 0, 10, 'train')
copy_files('cat', 0, 10, 'train')
copy_files('dog', 10, 14, 'test')
copy_files('cat', 10, 14, 'test')
"""

# 간단한 CNN으로 벤치마킹. 교재의 simple_cnn 모델
print("==========================")
print("====define cnn model======")
image_height, image_width = 150, 150
train_dir = os.path.join(work_dir+'data/', 'train')
test_dir = os.path.join(work_dir+'data/', 'test')
no_classes = 2
no_validation = 8 #800
epochs = 2
batch_size = 2 #200
no_train = 20 #2000
no_test = 8 #800
input_shape = (image_height, image_width, 3)
epoch_steps = no_train // batch_size # 여기가 0이 되어버리면
# AttributeError: 'ProgbarLogger' object has no attribute 'log_values' 에러 발생
test_steps = no_test // batch_size

def simple_cnn(input_shape):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(
        filters=75, # 64
        kernel_size=(3,3),
        activation='relu',
        input_shape=input_shape
        ))
    model.add(tf.keras.layers.Conv2D(
        filters=150, # 128
        kernel_size=(3,3),
        activation='relu',
        ))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(tf.keras.layers.Dropout(rate=0.3))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=32, activation='relu')) # 1024
    # tensorflow.python.framework.errors_impl.ResourceExhaustedError: OOM when allocating tensor with shape[799350,1024] and type float on /job:localhost/replica:0/task:0/device:CPU:0 by allocator cpu
    model.add(tf.keras.layers.Dropout(rate=0.3))
    model.add(tf.keras.layers.Dense(units=no_classes, activation='softmax'))
    model.compile(loss=tf.keras.losses.categorical_crossentropy,
                  optimizer=tf.keras.optimizers.Adam(),
                  metrics=['accuracy'])
    return model
simple_cnn_model = simple_cnn(input_shape)

# 한번에 이미지 묶음 하나씩만 로드.
# tf.keras에 ImageDataGenerator라는 클래스는 필요할 때마다 이미지를 읽음
#generator_train = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. /255)
generator_train = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1. / 255,
    horizontal_flip = True,
    zoom_range = 0.3,
    shear_range = 0.3,)
generator_test = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

# 디렉터리로부터 이미지를 읽어오는 flow_from_directory 메소드
train_images = generator_train.flow_from_directory(
    train_dir,
    batch_size = batch_size,
    target_size = (image_width, image_height))

test_images = generator_test.flow_from_directory(
    test_dir,
    batch_size = batch_size,
    target_size = (image_width, image_height))

# generator (생성기)는 모델을 학습시키기 위해 직접적으로 사용할 수 있다.
print("==========================")
print("====fitting cnn model=====")
simple_cnn_model.fit_generator(
    train_images,
    steps_per_epoch=epoch_steps,
    epochs=epochs,
    validation_data=test_images,
    validation_steps=test_steps)


    
