# -*- coding: utf-8 -*-
from .api import api
from .exceptions import *
from requests import post
 
class upload(object):
    def __init__(self, vk):
        if not isinstance(vk, api):
            raise mySword("arg must be api instance")
        self.vk = vk.call

    def audioMessage(self, filename, peer_id):
        url = self.vk("docs.getMessagesUploadServer", {'peer_id': peer_id, 'type': 'audio_message'})['upload_url']
        files = [('file', (filename, open(filename, 'rb')))]
        res = post(url, files=files).json()['file']
        saved = self.vk('docs.save', {'file': res})
        if "audio_message" in saved:
            return saved['audio_message']
        return saved
