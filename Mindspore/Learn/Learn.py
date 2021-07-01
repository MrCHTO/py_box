# 调用numpy模块
import numpy as np

# 调用mindspore模块
import mindspore

# 调用mindspore模块里的Tensor(张量)模块
from mindspore import Tensor

# 调用mindspore.ops模块里ops(算子)模块
import mindspore.ops as ops

# 调用mindspore模块里的dtype(类型)模块
from mindspore import dtype as mstype
from numpy.core.fromnumeric import shape

#  实例化张量
x = Tensor(np.array([1.0, 2.0, 3.0, 4.0]), mstype.float64)
y = mindspore.Tensor(np.array([[8, 4, 2, 1], [8, 4, 2, 1], [
                     8, 4, 2, 1], [8, 4, 2, 1]]), mindspore.int32)
z = mindspore.Tensor(np.array([[2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0], [
                     2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0]]), mstype.float64)

b1 = Tensor(np.array([True, True, True, False]), mindspore.bool_)
b2 = Tensor(np.array([[True, True], [False, False]]), mstype.bool_)

a = Tensor(np.ones(shape=[4, 2]), mindspore.float32)
b = Tensor(np.ones(shape=[2, 4]), mindspore.float32)

# 张量的算术运算
print(x, x+2, x-2, x*2, x**2)
print(y)
print(y+2)
print(z)
print(y*z)
print(b1)
print(b2)

# 张量的逻辑运算
# 与运算
print(b1.all(), b2.all())
# 或运算
print(b1.any(), b2.any())

# 张量的形状
print(x.shape, y.shape, z.shape)

# 张量的类型
print(x.dtype, y.dtype, z.dtype)

# 张量类型的转换(Tensor转Numpy)
print(x.asnumpy())

# 算子实例化Element-wise乘法
mul = ops.Mul()
res = mul(x, y)
print(res)

# 算子实例化矩阵乘法
matmul = ops.MatMul()
print(a)
print(b)
res = matmul(a, b)
print(res)

# 网络操作
input = Tensor(np.ones((2, 2)), mindspore.float32)
print(input)
