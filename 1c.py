import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

x= np.array([[25,0],[30,1],[45,2],[35,1],[50,0]])
y= np.array([0,1,1,1,0])

model=DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(x,y)
pre=model.predict([[60,2]])
print("prediction",pre)

plt.figure(figsize=(10,6))
tree.plot_tree(model,feature_names=["age","income"],class_names=["yes","no"],filled=True)
plt.show()
