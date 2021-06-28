# 向量运算符只在一个特定轴上运算，将一个向量映射到一个标量或者另外一个向量

# 实现了压缩第3个通道维度为1的通道

import numpy as np
import mindspore
from mindspore import Tensor
import mindspore.ops as ops

input_tensor = Tensor(np.ones(shape=[3, 2, 1]), mindspore.float32)
squeeze = ops.Squeeze(2)
output = squeeze(input_tensor)

print(output)
