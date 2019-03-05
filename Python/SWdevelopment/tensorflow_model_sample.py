def mymodel(train_url, test_url):
    print("---setting configurations---")
    import tensorflow as tf
    import csv
    # 데이터 로드
    train_data = []
    train_label = []
    with open(train_url, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # header jump
        for row in csvreader:
            line = list(map(int, row))
            train_label.append(line[0])
            train_data.append(line[1:])
        
    # 퍼셉트론 입력 크기, 클래스 수, 배치 크기, 반복 또는 배치의 총 개수 선언
    input_size = len(train_data[0])
    no_classes = len(set(train_label))
    batch_size = 100
    total_batches = 200

    # 원-핫 인코딩
    # train_label_hot = tf.one_hot(train_label, no_classes)

    train_label_hot = []
    for row in train_label:
        for num in range(no_classes):
            if row == num:
                one_hot = [0]*no_classes
                one_hot[num] = 1
                train_label_hot.append(one_hot)

    # 입력데이터와 타깃을 위한 플레이스홀더 정의 (None은 어떤 크기든 될 수 있음을 의미)
    x_input = tf.placeholder(tf.float32, shape=[None, input_size])
    y_input = tf.placeholder(tf.float32, shape=[None, no_classes])

    # 단순한 선형 분류자 또는 퍼셉트론을 정의
    weights = tf.Variable(tf.random_normal([input_size, no_classes]))
    bias = tf.Variable(tf.random_normal([no_classes]))
    logits = tf.matmul(x_input, weights) + bias

    # 퍼셉트론으로 생성된 로짓과 원-핫 레비을의 y_input을 비교
    # 비교는 교차 엔트로피와 함께 소프트맥스를 사용
    softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
        labels=y_input, logits=logits)
    loss_operation = tf.reduce_mean(softmax_cross_entropy)
    optimiser = tf.train.GradientDescentOptimizer(
        learning_rate=0.5).minimize(loss_operation)

    # 모델 훈련을 위한 세션 시작
    session = tf.Session()

    # 전역 변수 초기화 함수를 이용해 변수를 초기화
    print("---run model---")
    session.run(tf.global_variables_initializer())
    _, loss_value = session.run([optimiser, loss_operation], feed_dict={
        x_input: train_data,
        y_input: train_label_hot
    })
    print("loss: ", loss_value)

    # test 데이터 불러오기
    # 데이터 로드
    test_data = []
    with open(test_url, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # header jump
        for row in csvreader:
            test_data.append(list(map(int, row)))
        
    #test_data = pd.read_csv('C:\\Users\\BY\\Downloads\\test.csv', header=0)

    # 정확도를 계산
    predictions = tf.argmax(logits, 1)
    test_label = session.run([predictions], feed_dict={
        x_input: test_data
    })
    print("----saving data----")
    # with open
    # f_result.write("" %())
    save_url = test_url.split('/')[:-1]
    with open('/'.join(save_url)+'/submission.csv', mode='w', newline='\n') as csvfile:
        tensor_result = csv.writer(csvfile, delimiter=',')
        tensor_result.writerow(['ImageId', 'Label'])
        for line in range(len(test_label[0])):
            tensor_result.writerow([str(line+1), str(test_label[0][line])])

    #print('test_label : ', test_label[0])
    session.close()
    print("---session closed---")
