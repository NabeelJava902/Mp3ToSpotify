def parse(track_name):
    if '-' in track_name:
        artist = track_name.split("-", 1)[0][:-1]
        song_name = track_name.split("-", 1)[1]
        if ".mp3" in song_name:
            track_name = song_name[:-4]
        if '(' in song_name:
            track_name = song_name.split("(", 1)[0]
            track_name = track_name[1:-1]
        if '[' in song_name:
            track_name = song_name.split("[", 1)[0][:-1]
        dict = {
            'artist': f"{artist}",
            'track_name': f"{track_name}"
        }
    else:
        if ".mp3" in track_name:
            track_name = track_name[:-4]
        if '(' in track_name:
            track_name = track_name.split("(", 1)[0][:-1]
        dict = {
            'artist': None,
            'track_name': f"{track_name}"
        }
    return dict


def get_failure_rate(all_tracks, failed_tracks):
    return round((len(all_tracks)) / (len(failed_tracks)))