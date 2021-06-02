import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import numpy as np
import pandas as pd
import seaborn as sns
import pathlib

pd.set_option("display.max_columns", None)


def resolve_relative_path(file: str, path: str, parent_levels=0) -> pathlib.Path:
    """
    returns absolute path to a file given its relative :param path from :param file
    :param file: path from root to a file
    :param path: relative path to file2 from the last common point in the two paths
    :param parent_levels: number of levels in the path to go up to get to the last common point
    :return: path from root to file2
    """
    return pathlib.Path(file).parents[parent_levels].joinpath(path)


# auth:


# composer data:
composers_path = resolve_relative_path(
    __file__, "data/composer_era.csv", parent_levels=1
)
composers = pd.read_csv(composers_path)
print(composers.head())
