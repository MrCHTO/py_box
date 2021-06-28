# 张量的操作

# 张量的数学运算符可以分为标量运算符、向量运算符以及矩阵运算符。

# 加减乘除乘方，以及三角函数、指数、对数等常见函数，逻辑比较运算符等都是标量运算符。

# 标量运算符的特点是对张量实施逐元素运算。

# 有些标量运算符对常用的数学运算符进行了重载。并且支持类似NumPy的广播特性。

import numpy as np
import mindspore
from mindspore import Tensor

input_x = mindspore.Tensor(np.array([1.0, 2.0, 4.0]), mindspore.float32)
input_y = 3.0
print(input_x**input_y)
print(input_x + input_y)
