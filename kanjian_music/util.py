# -*- coding: utf-8 -*-

import hmac
import base64
from hashlib import sha1, md5

def generate_sig(app_secret, **kwargs):
    """
    通过私钥和参数生成sig
    """
    # 将除了 sig 以外的所有请求参数的原始值按照参数名的字典序排序
    params = sorted(kwargs.items(), key=lambda p: p[0])

    # 将排序后的参数键值对用&拼接，即拼成 key1=val1&key2=val2&...
    tmp_list = ["%s=%s" % (p[0], p[1]) for p in params]
    tmp_str = "&".join(tmp_list)

    # 将第二步骤得到的字符串进行 Base64 编码
    b64_str = base64.b64encode(bytes(tmp_str.encode("utf8")))

    # 将 app_secret 作为哈希 key 对第三步骤得到的 Base64 编码后的字符串进行 HMAC-SHA1 哈希运算得到字节数组
    sha1_str = hmac.new(app_secret.encode("utf8"), b64_str, sha1).digest()

    # 对第四步骤得到的字节数组进行 MD5 运算得到 32 位字符串，即为 sig
    m=md5()
    m.update(sha1_str)

    return m.hexdigest()
