import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 3, 5, 7])
Y = np.array([4, 2, 3, 1])

# 데이터 산점도
plt.scatter(X, Y)

# 선그래프 
plt.plot(X,Y)
plt.show()