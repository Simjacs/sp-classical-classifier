import pandas as pd
import numpy as np
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from keras.models import Sequential
from src.utils import resolve_relative_path, recombine_data

pd.set_option("display.max_columns", None)

# read data:
data_path = resolve_relative_path(__file__, "data", parent_levels=1)
df = recombine_data(data_path, file_name_format="timbres_0.pkl")
X = (df["timbres"])


# specify model:
input_channels = 12
input_length = None
model = Sequential()

model.add(Conv1D(filters=20, kernel_size=10, input_shape=(input_length, input_channels), activation="relu"))
model.add(Conv1D(filters=20, kernel_size=10, activation="relu"))
model.add(MaxPooling1D(pool_size=4))

model.add(Conv1D(filters=30, kernel_size=4, activation="relu"))
model.add(Conv1D(filters=30, kernel_size=4, activation="relu"))
model.add(MaxPooling1D(pool_size=8))

model.add(Flatten)

