"""
Step 1: Access folder containing mp3 files and copy MP3 titles and corresponding author onto text file
Step 2: Create playlist on Spotify
Step 3: Search for the song
Step 4: Add song onto new playlist. If song is not available, add title to a separate text file
Step 5: Get list of all unfindable songs
"""

from Project.spotify_api.spotify_client import *
from Project.spotify_api.variables import playlist_id
from Project.gen_functions import gen_list, retrieve
from Project.gen_util import get_failure_rate


class CreatePlaylist(object):

    def __init__(self):
        self.spotify = SpotifyAPI()
        pass

    # Step 1#
    def read_from_folder(self):
        gen_list()
        return retrieve()
        pass

    # Step 2#
    def create_playlist(self):
        name = "MP3 Songs"
        description = "All MP3 songs coming from an android smart phone"
        return self.spotify.create_playlist(name, description)  # Create playlist and set id value
        pass

    # Step 3#
    def get_spotify_URI(self, song_name=None, song_artist=None):
        return [self.spotify.get_track(query=song_name, artist=song_artist)['uri']]

    # Step 4#
    def add_song(self, playlist_id, track_uri_list):
        self.spotify.add_tracks_to_playlist(playlist_id, track_uri_list)

    # Step 5#
    def get_missing_songs(self, song_name, artist_name):
        dict = {
            "song": song_name,
            "artist_name": artist_name
        }
        return dict


missing_tracks = []
cp = CreatePlaylist()

mp3_list = cp.read_from_folder()
print("Generating playlist...")
for i in range (0, len(mp3_list)):
    try:
        artist = mp3_list[i]['artist']
    except KeyError:
        artist = None
    song = mp3_list[i]['track_name']
    uri = None
    try:
        uri = cp.get_spotify_URI(song_name=song, song_artist=artist)
    except:
        missing_tracks.append(cp.get_missing_songs(song, artist))
        continue
    cp.add_song(playlist_id, uri)
print("Playlist generated")
for x in range (0, len(missing_tracks)):
    print("Could not find " + missing_tracks[x]['song'])
print("Success rate = {}%".format((100-get_failure_rate(mp3_list, missing_tracks))))