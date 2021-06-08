import random

import pandas as pd
import numpy as np
from math import floor
# from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
# from keras.models import Sequential
from src.utils import resolve_relative_path, read_combined_data, standardise_timbre_length

pd.set_option("display.max_columns", None)

data_length = 300
# read data:
data_path = resolve_relative_path(__file__, "data", parent_levels=1)
combined_data_path = resolve_relative_path(__file__, "data/combined_timbres.pkl", parent_levels=1)
#df = read_combined_data(data_path)
#df.to_pickle(combined_data_path)
#df = read_combined_data(combined_data_path, already_combined=True)
df = pd.read_pickle(resolve_relative_path(__file__, "data/timbres_0.pkl", parent_levels=1))
#timbre_lengths = [len(row[i]["timbre"]) for row in ]

df["standard_len_timbres"] = df["timbres"].apply(lambda x: standardise_timbre_length(x, data_length))
X = (df["standard_len_timbres"])
timbre_lens = [len(timbre) for timbre in X]

print(pd.unique(timbre_lens))



# # specify model:
# input_channels = 12
# input_length = None
# model = Sequential()
#
# model.add(Conv1D(filters=20, kernel_size=10, input_shape=(input_length, input_channels), activation="relu"))
# model.add(Conv1D(filters=20, kernel_size=10, activation="relu"))
# model.add(MaxPooling1D(pool_size=4))
#
# model.add(Conv1D(filters=30, kernel_size=4, activation="relu"))
# model.add(Conv1D(filters=30, kernel_size=4, activation="relu"))
# model.add(MaxPooling1D(pool_size=8))
#
#
# model.add(Dense(3, activation="softmax"))
#
# model.compile(loss="categorical_crossentropy", optimizer="sgd")
#
# print(model)

