import numpy as np
from mindspore import Tensor
from mindspore import dtype as mstype

x = Tensor(np.array([[True, True], [False, False]]), mstype.bool_)

# all(axis, keep_dims)：在指定维度上通过and操作进行归约，axis代表归约维度，keep_dims表示是否保留归约后的维度
x_all = x.all()

# any(axis, keep_dims)：在指定维度上通过or操作进行归约，axis代表归约维度，keep_dims表示是否保留归约后的维度
x_any = x.any()

# asnumpy()：将Tensor转换为NumPy的array
x_array = x.asnumpy()

print(x_all, "\n\n", x_any, "\n\n", x_array)
