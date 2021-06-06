import pandas as pd
import datetime
from spotipy.exceptions import SpotifyException
from src.utils import SpotifyConnector, resolve_relative_path

pd.set_option("display.max_columns", None)

# auth:
connector = SpotifyConnector()

# composer data:
composers_path = resolve_relative_path(
    __file__, "data/composer_era.csv", parent_levels=1
)
composers = pd.read_csv(composers_path)
print(composers.head())

features = [
    "danceability",
    "energy",
    "key",
    "loudness",
    "mode",
    "valence",
    "tempo",
    "time_signature",
]
rows_list = []
timbre_rows_list = []
composer = 24

for i in range(composer, len(composers)):
    print(f"composer:{composer}")
    if i % 10 == 0:
        print(i)
    track_ids = []
    track_names = []
    name = f"{composers['firstnames'][i]} {composers['lastnames'][i]}"
    print(name)
    era = composers["era"][i]
    album_ids = connector.get_album_ids_from_name(name, "id")
    album_name = connector.get_album_ids_from_name(name, "name")
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
        if j % 100 == 0:
            print(
                f"track {j} out of {len(track_ids)}, composer {i} out of {len(composers)}"
            )
            print(str(datetime.datetime.now().time()))
        try:
            timbres = connector.get_track_timbres(track_ids[j])
            timbre_rows_list.append([track_ids[j], track_names[j], era, timbres])
        except SpotifyException:
            pass

    timbres_df = pd.DataFrame(
        columns=["track_id", "track_name", "era", "timbres"], data=timbre_rows_list
    )

    timbres_path = resolve_relative_path(
        __file__, f"data/timbres_{composer}.pkl", parent_levels=1
    )
    timbres_df.to_pickle(timbres_path)

    composer += 1
