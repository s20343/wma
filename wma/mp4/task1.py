import tensorflow as tf
import matplotlib.pyplot as plt

# Define the parameters
batch_size = 32
image_size = (150, 150)
epochs = 10  

# Set the path to the main_directory_500 folder
data_directory = 'C:/Users/PC/Desktop/wma/res'

# Load the images as a dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    data_directory,
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(150, 150),
    batch_size=batch_size
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    data_directory,
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(150, 150),
    batch_size=batch_size
)

class_names = train_dataset.class_names
num_classes = len(class_names)

# Configure the dataset for performance
train_dataset = train_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
val_dataset = val_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

# Create the CNN model
model = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=(image_size[0], image_size[1], 3)),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),  # Increase the number of filters
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),  
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),  
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),  # Increase the number of units
    tf.keras.layers.Dropout(0.5),  # Add dropout regularization
    tf.keras.layers.Dense(num_classes)
])

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),  # Adjust the learning rate
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=epochs
)

# Evaluate the model
loss, accuracy = model.evaluate(val_dataset)
print("Validation loss:", loss)
print("Validation accuracy:", accuracy)

# Plot training and validation accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Training', 'Validation'])
plt.show()

# Plot training and validation loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Training', 'Validation'])
plt.show()
