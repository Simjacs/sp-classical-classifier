import pandas as pd
from src.utils import resolve_relative_path

pd.set_option("display.max_columns", None)

data_path = resolve_relative_path(__file__, "data/timbres.csv", parent_levels=1)
data_pickle_path = resolve_relative_path(__file__, "data/timbres.pkl", parent_levels=1)
df = pd.read_pickle(data_pickle_path)
