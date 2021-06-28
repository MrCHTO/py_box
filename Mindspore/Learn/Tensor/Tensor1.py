# 张量
import numpy as np
from mindspore import Tensor
from mindspore import dtype as mstype

# Tensor(传入数据,数据类型)
x = Tensor(np.array([[1, 2], [3, 4]]), mstype.int32)
y = Tensor(1.0, mstype.int32)
z = Tensor(2, mstype.int32)
m = Tensor(True, mstype.bool_)
n = Tensor((1, 2, 3), mstype.int16)
p = Tensor([4.0, 5.0, 6.0], mstype.float64)
q = Tensor(p, mstype.float64)

print(x, "\n\n", y, "\n\n", z, "\n\n", m, "\n\n", n, "\n\n", p, "\n\n", q)
