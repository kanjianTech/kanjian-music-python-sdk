# -*- coding: utf-8 -*-

import json

import urllib.request
import urllib.parse

def get(url, params):
    """
    取得数据
    """
    params_str = urllib.parse.urlencode(params)
    req = urllib.request.Request(url="%s?%s" % (url, params_str))

    with urllib.request.urlopen(req) as f:
        rst = f.read().decode('utf-8')

    return json.loads(rst)
