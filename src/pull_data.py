import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import numpy as np
import pandas as pd
import seaborn as sns
from utils import SpotifyConnector, resolve_relative_path

pd.set_option("display.max_columns", None)

# auth:
connector = SpotifyConnector()

# composer data:
composers_path = resolve_relative_path(
    __file__, "data/composer_era.csv", parent_levels=1
)
composers = pd.read_csv(composers_path)
print(composers.head())


features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'valence', 'tempo', 'time_signature']
rows_list = []
timbre_rows_list = []

for i in range(len(composers[0:4])):
    name = f"{composers['firstnames'][i]} {composers['lastnames'][i]}"
    print(name)
    era = composers["era"][i]
    album_ids = connector.get_album_ids_from_name(name, "id")
    album_name = connector.get_album_ids_from_name(name, "name")
    track_ids = []
    track_names = []
    for album_id in album_ids:
        if album_id == "5OfGONHFJZD8xpz3gVBwYz":  # this is a specific bad album
            pass
        else:
            try:
                album_tracks = connector.get_album_track_ids(album_id, "id")
                album_track_names = connector.get_album_track_ids(album_id, "name")
                track_ids += album_tracks
                track_names += album_track_names
            except IndexError:
                pass

for j in range(len(track_ids)):
    # features_list = connector.get_audio_features_as_lists(track_ids[j], keys_list=features)
    # rows_list.append([track_ids[j]] + [track_names[j]] + features_list + [era])
    timbres = connector.get_track_timbres(track_ids[j])
    timbre_rows_list.append([track_ids[j], timbres])

timbres_df = pd.DataFrame(columns=["track_id", "timbres"],
                          data=timbre_rows_list)
timbres_path = resolve_relative_path(__file__, "data/timbres.json", parent_levels=1)
timbres_df.to_json(timbres_path)
print(timbres_df.dtypes)
