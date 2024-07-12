import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_price_prediction_model(train_data_path, model_save_path):
    data = pd.read_csv(train_data_path)
    X = data.drop('price', axis=1).values
    y = data['price'].values

    model = Sequential([
        Dense(64, activation='relu', input_shape=(X.shape[1],)),
        Dense(64, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=10, batch_size=32)
    model.save(model_save_path)

if __name__ == "__main__":
    train_data_path = '/workspaces/marketplace_listing/train_data/price_data.csv'
    model_save_path = '/workspaces/marketplace_listing/models/price_prediction_model.h5'
    train_price_prediction_model(train_data_path, model_save_path)
