import numpy as np

# 将列表转换成 ndarray
list1 = [3.14, 2.17, 0, 1, 2]
nd1 = np.array(list1)  # [3.14 2.17 0.   1.   2.  ]
print(nd1)
print(type(nd1))  # <class 'numpy.ndarray'>

list2 = [[3.14, 2.17, 0, 1, 2], [1, 2, 3, 4, 5]]
nd2 = np.array(list2)
print(nd2)
# [[3.14 2.17 0.   1.   2.  ]
#  [1.   2.   3.   4.   5.  ]]


# 利用 random 模块生成数组
nd3 = np.random.random([3, 3])
print(nd3)
# [[0.96924304 0.49947449 0.11222431]
#  [0.72800342 0.79133935 0.69944954]
#  [0.79807119 0.7390373  0.03063869]]
print("nd3 的形状为:", nd3.shape)
# nd3 的形状为: (3, 3)
print("nd3 的元素个数为:", nd3.size)
# nd3 的元素个数为: 9

np.random.seed(123)  # 设置随机种子
nd4 = np.random.randn(2, 3)  # 生成标准正态的随机数
print(nd4)
print("nd4 的形状为:", nd4.shape)
# nd4 的形状为: (2, 3)
np.random.shuffle(nd4)  # 随机打乱数据
print(nd4)
print(type(nd4))
# <class 'numpy.ndarray'>

v1 = np.arange(12)

print(v1.reshape(3, 4))  # 将v改成3行4列
print(v1.reshape(2, 6))  # 将v改成2行6列

# print(v[1:3])

v2 = np.arange(12).reshape(3, 4)
print(v2 @ v2.T)  # 矩阵乘法
print(v2 * v2)    # 对应元素相乘
