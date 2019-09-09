from sklearn.model_selection import train_test_split

# load data
X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.75, random_state=42)
X_test = test_df

from catboost import CatBoostClassifier, Pool, cv
from sklearn.metrics import accuracy_score

# CatBoost
model = CatBoostClassifier(
    custom_loss=['Accuracy'],
    random_seed=42,
    logging_level='Silent'
)

# training
model.fit(
    X_train, y_train,
    cat_features=categorical_features_indices,
    eval_set=(X_validation, y_validation),
#     logging_level='Verbose',  # you can uncomment this for text output
    plot=True
);


# 1. CatBoost 개념 확인
# 2. training 시 어떤 모델이 들어가는 것인지 확인
# 3. 결과 예측해서 accuracy score 뽑아내는 코드 찾기

# CatBoost tutorial: https://github.com/catboost/tutorials/blob/master/python_tutorial.ipynb
