import numpy as np
from mindspore import Tensor
from mindspore import dtype as mstype

x = Tensor(np.array([[1, 2], [3, 4]]), mstype.int32)

# 形状
x_shape = x.shape

# 数据类型
x_dtype = x.dtype

print(x_shape, x_dtype)
