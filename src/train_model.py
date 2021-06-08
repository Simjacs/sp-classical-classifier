import pandas as pd
import numpy as np
from math import floor
# from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
# from keras.models import Sequential
from src.utils import resolve_relative_path, read_combined_data

pd.set_option("display.max_columns", None)

# read data:
data_path = resolve_relative_path(__file__, "data", parent_levels=1)
combined_data_path = resolve_relative_path(__file__, "data/combined_timbres.pkl", parent_levels=1)
#df = read_combined_data(data_path)
#df.to_pickle(combined_data_path)
#df = read_combined_data(combined_data_path, already_combined=True)
df = pd.read_pickle(resolve_relative_path(__file__, "data/timbres_0.pkl", parent_levels=1))
#timbre_lengths = [len(row[i]["timbre"]) for row in ]

X = (df["timbres"])
timbre_lens = [len(timbre) for timbre in X]


def split_list(list_to_split, split_size):
    new_list = [list_to_split[i: i + split_size] for i in range(0, len(list_to_split), split_size)]
    return new_list


cut_off_quantile = 0.9
cut_off_len = np.quantile(timbre_lens, cut_off_quantile)
test_timbre = X[22]
test_timbre_len = len(test_timbre)
print(cut_off_len, test_timbre_len)
if test_timbre_len > cut_off_len:
    multiples = floor(test_timbre_len/cut_off_len)
    remainder = int(test_timbre_len % cut_off_len)
    exactly_divisible_list = test_timbre[:-remainder]
    last_average = np.mean(test_timbre[-remainder:], axis=0)
    split_timbres = split_list(exactly_divisible_list, multiples)
    averaged_timbres = [np.mean(timbres, axis=0) for timbres in split_timbres]
    timbres = averaged_timbres + last_average
elif test_timbre_len < cut_off_len:



print(len(test_timbre))


print(df.shape)



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

