# operations提供单个的Primitive(原始)算子。一个算子对应一个原语，是最小的执行对象，需要实例化之后使用

import numpy as np
import mindspore
from mindspore import Tensor
import mindspore.ops.operations as P

input_x = mindspore.Tensor(np.array([1.0, 2.0, 4.0]), mindspore.float32)
input_y = 3.0
pow = P.Pow()
output = pow(input_x, input_y)
print("output =", output)
