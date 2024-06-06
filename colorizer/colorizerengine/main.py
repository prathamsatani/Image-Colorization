from keras.models import load_model # type: ignore
import numpy as np
import base64
import cv2
import os

model = load_model(os.path.join(os.getcwd(),"colorizer","colorizerengine","ImageColorizer (4).keras"))

def encode_image(image):
    size = image.shape[0:2]
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  
    image = cv2.resize(image, (size[1]*2, size[0]*2), interpolation = cv2.INTER_AREA)
    image = image*255
    image = image.astype(np.uint8)
    _, buffer = cv2.imencode(".jpg", image)
    base64_string = base64.b64encode(buffer).decode("utf-8")
    return base64_string

def decode_image(base64_string):
    img_array = np.frombuffer(base64_string, dtype=np.uint8)
    image = cv2.imdecode(img_array, flags=cv2.IMREAD_COLOR)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (160, 160), interpolation = cv2.INTER_AREA)
    img = img.astype('float32') / 255.0 
    return img

def colorize_image(base64_string):
    image = decode_image(base64_string)
    predicted = np.clip(model.predict(image.reshape(1,160, 160,3)),0,255).reshape(160, 160,3)
    # predicted = cv2.cvtColor(predicted, cv2.COLOR_RGB2BGR)  
    # predicted = cv2.resize(predicted, (size[1]*2, size[0]*2), interpolation = cv2.INTER_AREA)
    predicted = encode_image(predicted)
    image = encode_image(image)
    return predicted, image
    