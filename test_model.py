from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a new simple model
new_model = Sequential()
new_model.add(Dense(units=64, activation='relu', input_dim=100))
new_model.add(Dense(units=10, activation='softmax'))

# Save the new model
new_model.save('models/test_model.h5')

print("New model created and saved successfully.")