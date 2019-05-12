from .api import api
from .exceptions import *
from .session import session as ses
from requests import post

class upload(object):
    def __init__(self, session):
        if not isinstance(session, ses):
            raise mySword("invalid session")
        self.vk = api(session).call

    def messageDocument(self, filename, peer_id, t='doc'):
        url = self.vk("docs.getMessagesUploadServer", {
        'peer_id': peer_id,
        'type': t
        })
        url = url['upload_url'] if not "error" in url else raise mySword(url['error_msg'])

        files = [('file', (filename, open(filename, 'rb')))]
        res = post(url, files=files).json()['file']

        return self.vk('docs.save', {'file': res})

    def audioMessage(self, filename, peer_id):
        return self.messageDocument(filename, peer_id, 'audio_message')

    def document(self, group_id=None):
        url = self.vk("docs.getMessagesUploadServer", {'group_id': group_id})
        url = url['upload_url'] if not "error" in url else raise mySword(url['error_msg'])

        files = [('file', (filename, open(filename, 'rb')))]
        res = post(url, files=files).json()['file']

        return self.vk('docs.save', {'file': res})

    def messagePhoto(self, filename, peer_id):
        url = self.vk("docs.getMessagesUploadServer", {'peer_id': peer_id})
        url = url['upload_url'] if not "error" in url else raise mySword(url['error_msg'])

        files = [('file', (filename, open(filename, 'rb')))]
        res = post(url, files=files).json()['file']

        return self.vk("photos.saveMessagesPhoto", {
        'photo': res['photo'],
        'server': res['server'],
        'hash': res['hash']
        })

    def albumPhoto(self, filename, album_id, group_id=None):
        res = self.vk("photos.getUploadServer", {
        'group_id': group_id,
        'album_id': album_id
        })
        url = res['upload_url'] if not "error" in res else raise mySword(url['error_msg'])

        files = [('file', (filename, open(filename, 'rb')))]
        res = post(url, files=files).json()

        return self.vk('photos.save', {
        'album_id': album_id,
        'group_id': group_id,
        'server': res['server'],
        'photos_list': res['photos_list'],
        'hash': res['hash']
        })

    def wallPhoto(self, filename, group_id=None, caption=None):
        res = self.vk("photos.getUploadServer", {'group_id': group_id})
        url = res['upload_url'] if not "error" in res else raise mySword(url['error_msg'])

        files = [('file', (filename, open(filename, 'rb')))]
        upl = post(url, files=files).json()

        return self.vk('photos.saveWallPhoto', {
        'group_id': group_id,
        'photo': upl['photo'],
        'server': upl['server'],
        'hash': upl['hash'],
        'caption': caption
        })
