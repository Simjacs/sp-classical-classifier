import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pathlib
import pandas as pd

def resolve_relative_path(file: str, path: str, parent_levels=0) -> str:
    """
    returns absolute path to a file given its relative :param path from :param file
    :param file: path from root to a file
    :param path: relative path to file2 from the last common point in the two paths
    :param parent_levels: number of levels in the path to go up to get to the last common point
    :return: path from root to file2
    """
    return str(pathlib.Path(file).parents[parent_levels].joinpath(path))


class SpotifyConnector:
    def __init__(self):
        self.cid = "2bd837c837174d50ab873c61acf24f68"
        self.secret = "033bb4a851d54615bf83aaf94239ee06"
        self.username = "omkwppodx5qi1pph0cwma65zc"
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=self.cid, client_secret=self.secret
        )
        self.sp = spotipy.Spotify(
            client_credentials_manager=self.client_credentials_manager
        )
        self.scope = "user-library-read playlist-read-private streaming user-modify-playback-state user-read-playback-state playlist-modify-private"
        self.token = util.prompt_for_user_token(
            self.username,
            self.scope,
            client_id=self.cid,
            client_secret=self.secret,
            redirect_uri="http://localhost/",
        )
        if self.token:
            self.sp = spotipy.Spotify(auth=self.token)
        else:
            print("Can't get token for", self.username)

    def get_artist_id_from_name(self, name: str, id_type: str):
        """id type can be ["genres", "name", "id", "uri"]"""
        search = self.sp.search(name, limit=1, type="artist")
        return search["artists"]["items"][0][id_type]

    def get_playlist_id_from_name(self, name: str) -> list:
        search = self.sp.search(name, limit=1, type="playlist")
        pl_id = search["playlists"]["items"][0]["id"]
        pl_name = search["playlists"]["items"][0]["name"]
        pl_uri = search["playlists"]["items"][0]["uri"]
        return [pl_id, pl_name, pl_uri]

    def get_essentials_album_ids_from_name(self, name: str, id_type: str):
        query = f"{name} essentials"
        search = self.sp.search(query, limit=10, type="album")["albums"]["items"]
        ids_list = [result[id_type] for result in search]
        return ids_list

    def get_album_ids_from_name(self, name: str, id_type: str) -> list:
        """takes composer fname + lname and returns up to 20 of their artist albums"""
        artist = self.get_artist_id_from_name(name=name, id_type="id")
        albums = self.sp.artist_albums(artist, limit=20)
        return [albums["items"][i]["id"] for i in range(len(albums["items"]))]

    def get_album_track_ids(self, album_id: str, id_type: str) -> list:
        """takes album id and returns list track [id_type]s"""
        tracks = self.sp.album_tracks(album_id)["items"]
        return [tracks[i][id_type] for i in range(len(tracks))]

    def get_playlist_track_ids(self, playlist_id: str, id_type: str) -> list:
        # id_type = ["uri", "name", "id"]
        tracks = self.sp.playlist_tracks(playlist_id)["items"]
        track_ids = [tracks[i]["track"][id_type] for i in range(len(tracks))]
        return track_ids

    def get_audio_features_as_lists(self, track_id: str, keys_list: list):
        track = self.sp.audio_features(track_id)
        features_list = []
        for key in keys_list:
            try:
                features_list.append(track[0][key])
            except:
                continue
        return features_list

    # TODO: does time matter? or just timbre?
    def get_track_timbres(self, track_id: str):
        analysis = self.sp.audio_analysis(track_id)
        timbres = [segment["timbre"] for segment in analysis["segments"]]
        return timbres

    def get_track_name_from_id(self, track_id: str):
        return self.sp.track(track_id)["name"]


def recombine_data(data_path: str, file_name_format="timbres_*.pkl") -> pd.DataFrame:
    for number, path in enumerate(pathlib.Path(data_path).rglob(file_name_format)):
        print(f"Reading pickle {number}")
        if number == 0:
            df = pd.read_pickle(path)
        else:
            df_to_concat = pd.read_pickle(path)
            df = pd.concat([df, df_to_concat])
    return df




