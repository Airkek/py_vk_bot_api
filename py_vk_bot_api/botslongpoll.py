from .api import api
from .session import session as ses
from .exceptions import *
from requests import post
from threading import Thread

eventTypes = [
"message_new",
"message_reply",
"message_edit",
"message_allow",
"message_deny",
"photo_new",
"photo_comment_new",
"photo_comment_edit",
"photo_comment_restore",
"photo_comment_delete",
"audio_new",
"video_new",
"video_comment_new",
"video_comment_edit",
"video_comment_restore",
"video_comment_delete",
"wall_post_new",
"wall_repost",
"wall_reply_new",
"wall_reply_edit",
"wall_reply_restore",
"wall_reply_delete",
"board_post_new",
"board_post_edit",
"board_post_restore",
"board_post_delete",
"market_comment_new",
"market_comment_edit",
"market_comment_restore",
"market_comment_delete",
"group_leave",
"group_join",
"user_block",
"user_unblock",
"poll_vote_new",
"group_officers_edit",
"group_change_settings",
"group_change_photo",
"vkpay_transaction"
]

class worker(Thread):
    def __init__(self, func, arg=None):
        Thread.__init__(self)
        self.func = func
        self.funcarg = arg
    def run(self):
        self.func(self.funcarg)

class botsLongPoll(object):
    polling = {}

    def __init__(self, session):
        if not isinstance(session, ses):
            raise mySword("invalid session")
        self.vk = api(session)

        self.group = self.vk.call("groups.getById")
        if "error" in self.group or len(self.group) == 0:
            raise mySword("this method is available only with group auth")
        self.group = self.group[0]

    def get(self):
        try:
            lp = post(self.server, data = {'act': 'a_check', 'key': self.key,'ts': self.ts, 'wait': 25}).json()
            self.ts = lp['ts']
            if len(lp['updates'])!=0:
                return lp['updates']
            raise mySword
        except:
            poll = self.vk.call("groups.getLongPollServer", {"group_id": self.group['id']})
            self.poll = poll
            self.server = poll['server']
            self.key = poll['key']
            self.ts = poll['ts']
            return self.get()

    def on(self, func):
        if func.__name__ in eventTypes:
            self.polling = {func.__name__: func, **self.polling}
            return
        else:
            raise TypeError("unknown event type")

    def __startPolling(self, none):
        while True:
            if self.stop:
                break
            for event in self.get():
                if not event['type'] in self.polling:
                    continue
                if event['type'] == "message_new":
                    event['object']['send'] = lambda message, args = {}: self.vk.call("messages.send", {"message": message, 'random_id': 0, 'peer_id': event['object']['peer_id'], **args})
                work = worker(self.polling[event['type']],event['object'])
                work.start()

    def startPolling(self):
        self.stop = False
        poll = worker(self.__startPolling)
        poll.start()

    def stopPolling(self):
        self.stop = True
