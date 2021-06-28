# 广播表示输入各变量channel数目不一致时，改变他们的channel数以得到结果

from mindspore import Tensor
import mindspore.ops as ops
import numpy as np

shape = (2, 3)
input_x = Tensor(np.array([1, 2, 3]).astype(np.float32))
broadcast_to = ops.BroadcastTo(shape)
output = broadcast_to(input_x)

print(output)
