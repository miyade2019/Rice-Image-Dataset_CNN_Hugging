import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Modeli yükle
model = load_model('rice_cnn_model.h5')

def process_image(img):
    # Görüntü boyutunu 64x64 olarak ayarlama
    img = img.resize((64, 64))
    img = np.array(img)
    img = img / 255.0  # Normalizasyon
    img = np.expand_dims(img, axis=0)  # Modelin beklediği giriş boyutuna uyum
    return img

# Uygulama başlığı
st.title("Prinç Türlerini Sınıflandırma :ear_of_rice: :rice:")
st.write("Resmi seç ve model pirincin türünü tahmin etsin.")

# Dosya yükleyici
file = st.file_uploader("Bir Resim Seç", type=['jpg', 'jpeg', 'png'])


if file is not None:
    img=Image.open(file)
    st.image(img,caption='Yüklenen Resim')
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

    class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
    st.write(class_names[predicted_class])