from requests import post
from .exceptions import *
from .session import session as ses

class api(object):
    def __init__(self, session, v='5.95'):
        if not isinstance(session, ses):
            raise mySword("invalid session")
        self.token = session.token
        self.ver = v

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
