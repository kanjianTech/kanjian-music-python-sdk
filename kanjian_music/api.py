# -*- coding: utf-8 -*-

import functools
import time
from urllib.parse import urljoin

from kanjian_music import client
from kanjian_music import util


class Api:

    def __init__(self, app_key, app_secret, server_host):
        self.app_key = app_key
        self.app_secret = app_secret
        self.server_host = server_host
        self._token = None

    def token(self):
        """
        获取token
        """
        url = urljoin(self.server_host, "/v1/token")
        now = int(time.time()*1000)

        if not self._token:
            params = {"app_key": self.app_key,
                      "timestamp": now}
            sig = util.generate_sig(self.app_secret, **params)
            params.update(sig=sig)
            self._token = client.get(url, params)
            self._token["expires_at"] = now + self._token["expires_in"] * 1000

        if "expires_at" in self._token and self._token["expires_at"] > now + 10 * 1000:
            params = {"app_key": self.app_key,
                      "timestamp": now}
            sig = util.generate_sig(self.app_secret, **params)
            params.update(sig=sig)
            self._token = client.get(url, params)
            self._token["expires_at"] = now + self._token["expires_in"] * 1000

        return self._token["access_token"]

    def genre_list(self, device_id, page, count):
        """
        获取基因列表
        """
        url = urljoin(self.server_host, "/v1/genre")
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def album_list_by_genre(self, device_id, page, count, genre_id):
        """
        通过基因id获取专辑
        """
        url = urljoin(self.server_host, "/v1/genre/%s/album" % genre_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def track_list_by_genre(self, device_id, page, count, genre_id):
        """
        通过基因id获取单曲
        """
        url = urljoin(self.server_host, "/v1/genre/%s/track" % genre_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def artist_list(self, device_id, page, count):
        """
        获取音乐人
        """
        url = urljoin(self.server_host, "/v1/artist")
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def album_list_by_artist(self, device_id, page, count, artist_id):
        """
        通过音乐人id获取专辑
        """
        url = urljoin(self.server_host, "/v1/artist/%s/album" % artist_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def track_list_by_artist(self, device_id, page, count, artist_id):
        """
        通过音乐人id获取单曲
        """
        url = urljoin(self.server_host, "/v1/artist/%s/track" % artist_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def album_detail(self, device_id, album_id):
        """
        通过专辑id获取专辑详细信息
        """
        url = urljoin(self.server_host, "/v1/album/%s" % album_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def track_list_by_album(self, device_id, page, count, album_id):
        """
        通过单曲列表获取专辑id
        """
        url = urljoin(self.server_host, "/v1/album/%s/track" % album_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "page": page, "count": count}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def track_detail(self, device_id, track_id):
        """
        通过单曲id获取单曲详细信息
        """
        url = urljoin(self.server_host, "/v1/track/%s" % track_id)
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def search_artist(self, device_id, page, count, keyword):
        """
        搜索音乐人
        """
        url = urljoin(self.server_host, "/v1/search/artist")
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "keyword": keyword}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def search_album(self, device_id, page, count, keyword):
        """
        搜索专辑
        """
        url = urljoin(self.server_host, "/v1/search/album")
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "keyword": keyword}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)

    def search_track(self, device_id, page, count, keyword):
        """
        搜索单曲
        """
        url = urljoin(self.server_host, "/v1/search/track")
        token = self.token()
        params = {"app_key": self.app_key, "access_token": token,
                  "device_id": device_id, "keyword": keyword}
        sig = util.generate_sig(self.app_secret, **params)
        params.update(sig=sig)
        return client.get(url, params)
