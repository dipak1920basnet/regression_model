from univariate_linear_regression import linear_model, X,y
import matplotlib.pyplot as plt 


print(y)
print(linear_model)

plt.scatter(X,y)
plt.plot(X,linear_model)
plt.show()

