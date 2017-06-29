# -*- coding: utf-8 -*-

from kanjian_music.api import Api

api = Api(app_key="app_key",
          app_secret="app_secret",
          server_host="http://server_host")

print("test token")
print(api.token())
print("test token")

print("test genre_list")
print(api.genre_list("1212", 0, 20))
print("test genre_list")

print("test album_list_by_genre")
print(api.album_list_by_genre("1212", 0, 20, 1))
print("test album_list_by_genre")

print("test track_list_by_genre")
print(api.track_list_by_genre("1212", 0, 20, 1))
print("test track_list_by_genre")

print("test artist_list")
print(api.artist_list("1212", 0, 20))
print("test artist_list")

print("test album_list_by_artist")
print(api.album_list_by_artist("1212", 0, 20, 1))
print("test album_list_by_artist")

print("test track_list_by_artist")
print(api.track_list_by_artist("1212", 0, 20, 1))
print("test track_list_by_artist")

print("test album_detail")
print(api.album_detail("1212", 1))
print("test album_detail")

print("test track_list_by_album")
print(api.track_list_by_album("1212", 0, 20, 1))
print("test track_list_by_album")

print("test track_detail")
print(api.track_detail("1212", 1))
print("test track_detail")

print("test search_artist")
print(api.search_artist("1212", 0, 20, "love"))
print("test search_artist")

print("test search_album")
print(api.search_album("1212", 0, 20, "love"))
print("test search_album")

print("test search_track")
print(api.search_track("1212", 0, 20, "love"))
print("test search_track")
