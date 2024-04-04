import numpy as np

#
# test_array = np.arange(1, 11)
# print(test_array)
#
# # test_array = np.arange(1, 11).reshape(3, 4)
# # print(test_array)
#
# test_array = np.arange(1, 13).reshape(3, 4)
# third_array = np.array([test_array,test_array,test_array])
# print(third_array)
# print(third_array.sum(axis=0)) #차원의 맨 앞에 것(깊이)
# print(third_array.sum(axis=1))
# print(third_array.sum(axis=2))
#
# test_array = np.arange(1, 13).reshape(3, 4)
# print(test_array.mean(axis=1))
# print(test_array.mean(axis=0))
# print(test_array.mean())
#
# print(test_array.std())
# print(test_array.std(axis=0))

# v1 = np.array([1,2,3])
# v2 = np.array([4,5,6])
# #v스택 수직으로 붙이는 것
# print(np.vstack((v1,v2)))
# #h스택 수평으로 붙이는 것
# print(np.hstack((v1,v2)))
#
# array1 = np.array([[1,2],
#                    [3,4]])
# array2 = np.array([[5,6],
#                    [7,8]])
#
# result = np.vstack((array1,array2))
# print(result)
# result = np.hstack((array1,array2))
# print(result)
#
# v1=v1.reshape(-1, 1)
# v2=v2.reshape(-1, 1)
# print(v1)
# print(v2)
# print(np.hstack((v1,v2)))
#
# v1=np.array([[1,2,3]])
# v2=np.array([[4,5,6]])
# print(np.concatenate((v1,v2),axis=0))
# print(np.concatenate((v1,v2),axis=1))
#
#
# v1=np.array([1,2,3,4]).reshape(2,2)
# print(v1)
#
# v2=np.array([[5,6]])
# print(v2)
#
# print(np.concatenate((v1,v2),axis=0))
# v2=np.array([[5,6]]).T #행렬을 변환 1행이면 1열로 변환
# print(v2)
# print(np.concatenate((v1,v2),axis=1))

# x = np.arange(1, 7).reshape(2,3)
# print(x)
# print(x+x)
# print(x-x)
# print(x/x)
# print(x**x)
#
# x_1 = np.arange(1, 7).reshape(2,3)
# x_2 = np.arange(1, 7).reshape(3,2)
# print(x_1)
# print(x_2)
# print(x_1.dot(x_2))
#
# x = np.arange(1, 13).reshape(4,3)
# y = np.arange(10, 40, 10)
# print(x)
# print(y)
# print(x+y)

