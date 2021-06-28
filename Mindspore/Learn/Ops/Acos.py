# 实现了Acos

import numpy as np
import mindspore
from mindspore import Tensor
import mindspore.ops as ops

acos = ops.ACos()
input_x = Tensor(np.array([0.74, 0.04, 0.30, 0.56]), mindspore.float32)
output = acos(input_x)
print(output)
