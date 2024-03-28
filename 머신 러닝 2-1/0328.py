import numpy as np
# for x,name in enumerate(['수박','참외','자두']):
#     print(x,name)

# num = [1,2,3]
# char = ['a','b','c']
# list(zip(num,char))
#
# dict(zip(num,char))
# print(dict(zip(num,char)))

# import random
# for i in range(10):
#     x=random.random()
#     print(x)
# print(random.randint(5,100))
#
# num = [1,2,3,4,5,6]
# print(random.choice(num))

# words = ['apple', 'banana', 'cherry','orange']
# word_len = list(map(len,words))
# print(word_len)
# #len 단어의 길이

# def max1(num1,num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
#
# x = int(input("num1 : "))
# y = int(input("num2 : "))
# print(max1(x,y))

# def plusfive(x):
#     return x+5
# print(plusfive(20))
#
# plus_five = lambda x: x+5
# print(plus_five(20))

# def plusfive(x):
#     return x + 5
# list(map(plusfive,[15,25,35]))
##한줄로 변경
# list(map(lambda x:x+5,[15,25,35]))

# # #이메일에서 gmail만 출력하게끔
# emails = ['ex@gmail.com','user@naver.com','info@gmail.com','test@daum.net']
# gmail_list = list(filter(lambda e:e.endswith('@gmail.com'),emails))
# print(gmail_list)

# import pandas as pd
#
# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
# df_data = pd.read_csv(data_url, sep='\s+', header=None)
# df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV']
# print(df_data.head())
#
# df_data['weight_0']=1
# df_data.head()
#
# # MEDV 열을 삭제
# df_data = df_data.drop("MEDV", axis=1)
# df_data.head(5)
#
# df_matrix = df_data.values
# print(df_matrix)
#
# import numpy as np
# weight_vector = np.random.random_sample((14,1))
# print(weight_vector)

# import numpy as np
# x = np.array([1,2,5,8],float)
# print(x)
# print(type(x))
# print(x.dtype)
#
# x = np.array([1,2,5,"8"],float)
# print(x)
# print(x[3].dtype)
#
# print(x.shape)
#
# y = np.array([[1,2,5,8],[1,2,5,8],[1,2,5,8]])
# np.array(y,int)
# print(y.shape)
#
# x = np.array(y, int)
# print(x)
# print(x.shape)
#
# tensor_rank3 = [
#     [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
#     [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
#     [[1,2,5,8],[1,2,5,8],[1,2,5,8]]
# ]
# x = np.array(tensor_rank3, int)
# print(x)
# print(x.shape)
# print(x.ndim)
# print(x.size)
#
# x = np.array([[1,2,3.5],[4,5,6.5]], dtype=float)
# print(x)
#
# import sys
# x = np.array([[1,2,3.5],[4,5,6.5]], dtype=np.float_)
# print(x.itemsize)
#
# x = np.array([[1,2,3.5],[4,5,6.5]],int)
# print(x.shape)
# y = x.reshape(-1,)
# z = x.reshape(-1, 2)
# print(y)
# print(z)
#
# x = np.array(range(8))
# print(x.reshape(2,2,-1))
# #1차원으로 변경
# print(x.flatten())
#
# x = np.array([[1,2,3],[4.5,5,6]],int)
# print(x)
#
# print(x[0][0])
# print(x[0][1])
# x[0,1]=100
# print(x)

# 인덱싱, 슬라이싱
# x = np.array([[1, 2, 3, 4, 5] , [6 ,7 ,8 ,9 ,10]],int)
# print(x[:2:])
# print(x[1:3])
# print(x[1,1:3])
#
# x = np.array(range(15),int).reshape(3,-1)
# print(x)
# print(x[:,::2])
# print(x[::2,::3])

# x = np.arange(10)
# print(x)

# x = np.arange(-5,5)
# print(x)
# x = np.arange(0,5,0.5)
# print(x)
#
# #1 데이터 생성
# x = np.ones(shape=(5,2),dtype=np.int8)
# print(x)
# #0 데이터 생성
# x = np.zeros(shape=(2,2),dtype=np.float32)
# print(x)
#
# x = np.empty(shape=(2,4),dtype=np.float32)
# print(x)
#
# x = np.arange(12).reshape(3,4)
# print(x)
#
# x = np.ones_like(x)
# print(x)
#
# x = np.zeros_like(x)
# print(x)

# x = np.identity(n=3, dtype=int)
# print(x)
#
# x = np.identity(n=4, dtype=int)
# print(x)
#
# x = np.eye(N=3, M=5)
# print(x)
#
# x = np.eye(N=3, M=5, k=2)
# print(x)
#
#
# y = np.arange(9).reshape(3,3)
# print(y)
#
# #대각선 값 뽑아오기
# z = np.diag(y)
# print(z)
#
# z = np.diag(y,k=1)
# print(z)

# x = np.random.uniform(0,5,10)
# print(x)
#
# x = np.random.normal(0,2,10)
# print(x)

