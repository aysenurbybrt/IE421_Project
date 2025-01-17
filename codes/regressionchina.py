import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

file_path = 'soru 3 data.csv' 
data = pd.read_csv(file_path)

china_data = data[data['Entity'] == 'China']

X = china_data[['Year']].values 
y = china_data['Annual CO₂ emissions'].values 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Predicted')
plt.title('China Annual CO₂ Emissions')
plt.xlabel('Year')
plt.ylabel('Annual CO₂ Emissions (tons)')
plt.legend()
plt.show()
