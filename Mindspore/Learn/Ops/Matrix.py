# 矩阵运算包括矩阵乘法、矩阵范数、矩阵行列式、矩阵求特征值、矩阵分解等运算

# 实现了input_x和input_y的矩阵乘法

import numpy as np
import mindspore
from mindspore import Tensor
import mindspore.ops as ops

input_x = Tensor(np.ones(shape=[1, 3]), mindspore.float32)
input_y = Tensor(np.ones(shape=[3, 4]), mindspore.float32)
matmul = ops.MatMul()
output = matmul(input_x, input_y)

print(output)
