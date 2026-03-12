import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x= np.array([1000,1500,2000,2500,3000]).reshape(-1,1)
y= np.array([150000,200000,250000,300000,350000])

model=LinearRegression()
model.fit(x,y)

print("Intercept",model.intercept_)
print("slope",model.coef_[0])

prediction=model.predict([[2200]])
print("Prediction",prediction)

plt.scatter(x,y,color="blue",label="actual data")
plt.plot(x,model.predict(x),color="red",label="regression")
plt.scatter(2200,prediction,color="green",label="predicted price")
plt.xlabel("sqyare foot")
plt.ylabel("price")
plt.legend()
plt.show()
