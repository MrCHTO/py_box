# composite提供一些预定义的组合算子，以及复杂的涉及图变换的算子，如GradOperation

from mindspore import dtype as mstype
from mindspore.ops import composite as C
from mindspore import Tensor

mean = Tensor(1.0, mstype.float32)
stddev = Tensor(1.0, mstype.float32)
output = C.normal((2, 3), mean, stddev, seed=5)
print("output =", output)
