# 实现了Element-wise乘法

import numpy as np
import mindspore
from mindspore import Tensor
import mindspore.ops as ops

input_x = Tensor(np.array([1.0, 2.0, 3.0]), mindspore.float32)
input_y = Tensor(np.array([4.0, 5.0, 6.0]), mindspore.float32)
mul = ops.Mul()
res = mul(input_x, input_y)

print(res)
