from .api import api
from .session import session as ses
from .exceptions import mySword
from threading import Thread
import requests

class botsLongPoll(object):
    polling = {}
    ts = 0

    def __init__(self, session):
        if not isinstance(session, ses):
            raise mySword("invalid session")

        self.vk = api(session)
        group = self.vk.call("groups.getById")

        if 'error' in group or len(group) == 0:
            raise mySword("this method is available only with group auth")

        self.group = group[0]
        self.__getServer()

    def __getServer(self):
        poll = self.vk.call("groups.getLongPollServer", {"group_id": self.group['id']})
        self.server = poll['server']
        self.key = poll['key']
        self.ts = poll['ts']

    def get(self):
        try:
            lp = requests.post(self.server, data = {'act': 'a_check', 'key': self.key,'ts': self.ts, 'wait': 25}).json()
            self.ts = lp['ts']

            if 'updates' in lp:
                return lp['updates']

            raise mySword
        except:
            self.__getServer()
            return self.get()

    def on(self, func):
        self.polling[func.__name__] = func

    def __startPolling(self):
        while not self.stop:
            for event in self.get():
                if event['type'] in self.polling:
                    if event['type'] == "message_new":
                        try:
                            event['object']['send'] = lambda message, args = {}: self.vk.call("messages.send", {"message": message, 'random_id': 0, 'peer_id': event['object']['peer_id'], **args})
                        except:
                            pass

                    work = Thread(target=self.polling[event['type']], args=[event['object']])
                    work.start()

    def startPolling(self):
        self.stop = False

        poll = Thread(target=self.__startPolling)
        poll.start()

    def stopPolling(self):
        self.stop = True
