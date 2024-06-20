import tensorflow as tf
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout

# Definisikan daftar kelas yang sesuai dengan proyek Anda
classes = {0: 'battery', 1: 'glass', 2: 'metal', 3: 'organic', 4: 'paper', 5: 'plastic'}  # Gantilah dengan daftar kelas yang Anda miliki

# Definisikan base model
base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Tambahkan layer tambahan di atas base model
x = base_model.output
x = GlobalAveragePooling2D(name='avg_pool')(x)
x = Dense(1024, activation='relu', name='fc1')(x)
x = Dropout(0.5, name='dropout')(x)
predictions = Dense(len(classes), activation='softmax', name='predictions')(x)

# Definisikan model
model = Model(inputs=base_model.input, outputs=predictions)

# Fine-tuning: Membekukan layer di base model kecuali beberapa layer terakhir
for layer in base_model.layers[:-50]:
    layer.trainable = False

# Kompilasi model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Simpan model dengan nama layer yang telah diperbaiki
model.save('D:/Kuliah/MSIB/Hactiv8id/Capstone/PROJECT/deployment_capstone/final_densenet_model_fix.h5')
