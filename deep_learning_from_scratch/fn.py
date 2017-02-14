# common functions
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 개선된 softmax
def softmax(a):
    max_value = np.max(a)
    exp_a = np.exp(a - max_value)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

# 교차 엔트로피 오차 (CEE)
def cross_entropy_error(y, t):
    delta = 1e-7  # np.log 에  0 입력시, 마이너스 무한대(-inf)가 출력되기 때문에, 아주 작은 값을 더해 0이 되지 않도록 함
    return -np.sum(t * np.log(y + delta))

# 교차 엔트로피 오차 (CEE)
# 미니배치도 사용가능하도록 변경
# for one-hot encoding
def cross_entropy_error_one_hot(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size

# 교차 엔트로피 오차 (CEE)
# 미니배치도 사용가능하도록 변경
# for one-hot encoding
def cross_entropy_error_number_label(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size

# 평균 제곱 오차 (MSE)
def mean_squred_error(y, t):
    return 0.5 * np.sum((y-t)**2)
