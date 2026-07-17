from tensorflow.keras.models import load_model

try:
    model = load_model(r"C:\Users\Global\Crop Disease Detection System\models\mobilenet_final.keras")
    print("Model loaded successfully!")
except Exception as e:
    import traceback
    traceback.print_exc()