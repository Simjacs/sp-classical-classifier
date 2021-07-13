import random
import pandas as pd
import logging
import numpy as np
from tensorflow import convert_to_tensor
from math import floor
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from utils import Utils, standardise_timbre_length

pd.set_option("display.max_columns", None)

data_length = 300
# read data:
logging.info("Reading data")
data_path = Utils.resolve_relative_path(__file__, "data", parent_levels=1)
combined_data_path = Utils.resolve_relative_path(__file__, "data/combined_timbres.pkl", parent_levels=1)
df = Utils.create_sample_data(data_path)
# df = Utils.read_combined_data(data_path, already_combined=False)
# df.to_pickle(Utils.join_string_path(data_path, "combined_timbres.pkl"))
# df = Utils.read_combined_data(combined_data_path, already_combined=True)
print("data shape:", df.shape)
# df = Utils.create_sample_data(data_path)

# process data:
df["standard_len_timbres"] = df["timbres"].apply(lambda x: standardise_timbre_length(x, data_length))
df["standard_len_timbres"] = df["standard_len_timbres"].apply(lambda x: np.asarray(x).astype('float32'))
df["era_encode"] = df["era"].replace({"baroque": 0, "classical": 1, "romantic": 2})
X = np.asarray(df["standard_len_timbres"])
y = df["era_encode"].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
X_train = Utils.reformat_array(X_train)
X_test = Utils.reformat_array(X_test)
y_train = to_categorical(y_train, 3)
y_test = to_categorical(y_test, 3)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# specify model:
input_channels = 12
model = Sequential()

model.add(Conv1D(filters=24, kernel_size=11, input_shape=(data_length, input_channels), activation="relu"))
model.add(Conv1D(filters=36, kernel_size=13, activation="relu"))
model.add(MaxPooling1D(pool_size=13, strides=5))

model.add(Conv1D(filters=40, kernel_size=4, activation="relu"))
model.add(Conv1D(filters=48, kernel_size=12, activation="relu"))
model.add(MaxPooling1D(pool_size=10, strides=5))

model.add(Flatten())
model.add(Dense(432, activation="relu"))
model.add(Dense(40, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="sgd")

[print(i.shape, i.dtype) for i in model.inputs]


# fit model:
model.fit(X_train, y_train)

# predict model:
predictions = model.predict(X_test)

# evaluate model:
print("model evaluation:", model.evaluate(X_test, y_test))
