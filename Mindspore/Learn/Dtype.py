from mindspore import dtype as mstype

# 将MindSpore的数据类型转换为NumPy对应的数据类型
np_type = mstype.dtype_to_nptype(mstype.int32)

# 将Python内置的数据类型转换为MindSpore对应的数据类型
ms_type = mstype.pytype_to_dtype(int)

# 将MindSpore的数据类型转换为Python对应的内置数据类型
py_type = mstype.dtype_to_pytype(mstype.float64)

print(np_type)
print(ms_type)
print(py_type)
