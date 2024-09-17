# scripts/statistical_modeling.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

def load_data(path):
    # Utility function to load data
    return pd.read_csv(path)

def preprocess_data(df):
    # Handle missing data (imputation or removal)
    df = df.dropna()
    
    # Encoding categorical variables
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    categorical_cols = ['Province', 'ZipCode', 'CoverType']
    encoded = pd.DataFrame(encoder.fit_transform(df[categorical_cols]))
    
    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df, encoded], axis=1)
    
    return df

def build_models(df):
    # Split into train/test sets
    X = df.drop(['TotalPremium', 'TotalClaims'], axis=1)
    y = df['TotalPremium']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    
    # Random Forest
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train, y_train)
    
    # XGBoost
    xg_model = xgb.XGBRegressor()
    xg_model.fit(X_train, y_train)
    
    # Evaluate models
    models = {'Linear Regression': lr_model, 'Random Forest': rf_model, 'XGBoost': xg_model}
    return models, X_test, y_test

def evaluate_models(models, X_test, y_test):
    for name, model in models.items():
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print(f"{name} - MSE: {mse}, R2: {r2}")

# Example usage
if __name__ == "__main__":
    df = load_data('../data/your_data.csv')
    df = preprocess_data(df)
    models, X_test, y_test = build_models(df)
    evaluate_models(models, X_test, y_test)
