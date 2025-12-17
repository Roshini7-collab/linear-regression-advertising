from linear_regression import (
    load_advertising_data,
    train_linear_model,
    regression_metrics
)
from sklearn.model_selection import train_test_split

df = load_advertising_data("data/advertising.csv")

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = train_linear_model(X_train, y_train)
y_pred = model.predict(X_test)

metrics = regression_metrics(y_test, y_pred)
print(metrics)
