# functional提供operations和composite实例化后的对象，简化算子的调用流程

import numpy as np
import mindspore
from mindspore import Tensor
from mindspore.ops import functional as F

input_x = mindspore.Tensor(np.array([1.0, 2.0, 4.0]), mindspore.float32)
input_y = 3.0
output = F.tensor_pow(input_x, input_y)
print("output =", output)
