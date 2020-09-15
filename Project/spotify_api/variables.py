spotify_client_id = "(input client_id)"
spotify_secret = "(input spotify_secret)"
spotify_user_id = "(input user_id)"
# Put playlist_id here after you use the create_playlist function
playlist_id = ""

import pickle
import os


class SaveLoad(object):
    user_access_token = None
    user_refresh_token = None
    did_access_token_expire = True
    dir_path = '(add root paths)/Project/spotify_api'
    r_w_path = 'dump.txt'

    def save_tokens(self):
        os.chdir(self.dir_path)
        dict = {
            "access": f"{self.user_access_token}",
            "refresh": f"{self.user_refresh_token}",
            "expire": f"{self.did_access_token_expire}"
        }
        file = open(self.r_w_path, 'wb')
        pickle.dump(dict, file)
        file.close()

    def reload(self):
        os.chdir(self.dir_path)
        file = open(self.r_w_path, 'rb')
        dict = None
        try:
            dict = pickle.load(file)
        except EOFError:
            self.did_access_token_expire = True
        if dict is not None:
            self.user_access_token = dict['access']
            self.user_refresh_token = dict['refresh']
            self.did_access_token_expire = dict['expire']
        file.close()

    def set_tokens(self, access, refresh):
        self.user_refresh_token = refresh
        self.user_access_token = access

    def clear_file(self):
        os.chdir(self.dir_path)
        file = open(self.r_w_path, 'r+')
        file.truncate(0)
        file.close()
