import numpy as np
from tensorflow.keras.models import load_model
from app.classes import classes
from app.utils import preprocess_image

# model load (start me ek baar load hoga)
model = load_model("model/mobilenet_best.h5")

def predict_image(file):
    image = preprocess_image(file.file)

    preds = model.predict(image)
    index = int(np.argmax(preds))
    confidence = float(np.max(preds))

    return {
        "breed": classes[index],
        "confidence": round(confidence, 2)
    }