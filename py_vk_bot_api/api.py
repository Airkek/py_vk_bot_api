# -*- coding: utf-8 -*-
from requests import post
from .exceptions import *
 
class api:
    def __init__(self, token, v='5.95'):
        self.token = token
        self.ver = v
        if "error" in post("https://api.vk.com/method/users.get", {'access_token': self.token, 'v': self.ver, 'user_ids': 1}).json():
            raise mySword("invalid token")

    def call(self, method, params={}):
        res = post(f"https://api.vk.com/method/{method}", {'access_token': self.token, 'v': self.ver, **params}).json()
        if not "error" in res:
            return res['response']
        return res

    def parseuid(self, text):
        try:
            if "vk.com/" in text:
                u = (text.split("vk.com/")[1]+" ").split(" ")[0]
                u = u.split("/")[0] if "/" in u else u
            else:
                u = text.strip()
            try:
                return self.call("users.get", {'user_ids': u})[0]['id']
            except:
                return -self.call("groups.getById", {'group_ids': u})[0]['id']

        except:
            return None
