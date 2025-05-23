"""
@author: Ritalin
problem:  MV Linear Regression with diabetes
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabet = load_diabetes()
X = diabet.data
y = diabet.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred = lin_reg.predict(X_test)

# False olursa rmse olur
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"mse skoru: {rmse}")
