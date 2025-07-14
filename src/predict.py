from tensorflow.keras.models import load_model
import numpy as np

model = load_model("model/churn_model.h5")

def predict_customer(data):
    return model.predict(np.array([data]))[0][0]
