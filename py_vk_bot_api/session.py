from .exceptions import authError
import re
import requests

class session(object):
    def __init__(self, token, http=None):
        self.token = token

        if "error" in requests.post("https://api.vk.com/method/users.get", {'access_token': self.token, 'v': '5.95', 'user_ids': 1}).json():
            raise authError("invalid token")

def userAuth(login, password, appid=2685278, scope=1073737727):
    s = requests.Session()
    s.headers.update({'User-agent': 'Mozilla/5.0 (py_vk_bot_api; Airkek; Python) AppleWebKit/537.36 (KHTML, like Gecko)'})

    res = s.get('https://vk.com/')
    val = {
        'act': 'login',
        'role': 'al_frame',
        '_origin': 'https://vk.com',
        'utf8': '1',
        'email': login,
        'pass': password,
        'lg_h': re.compile(r'name="lg_h" value="([a-z0-9]+)"').search(res.text).groups()[0]
    }

    res = s.post('https://login.vk.com/', val)
    if 'Captcha' in res.text:
        raise authError('captcha ;c')

    if 'onLoginFailed(4' in res.text:
        raise authError('invalid password')

    if 'act=authcheck' in res.text:
        raise authError('unknown error. Please, open issue on github (Airkek/py_vk_bot_api)')

    if 'security_check' in res.url:
        raise authError('security check is required ;c. Try to log-in with token')

    if 'act=blocked' in res.url:
        raise authError('account is blocked')

    res = s.post('https://oauth.vk.com/authorize', {
        'client_id': appid,
        'scope': scope,
        'response_type': 'token',
        'revoke': '1',
    })

    if 'access_token' not in res.url:
        url = re.compile(r'location\.href = "(.*?)"\+addr;').search(res.text).groups()[0]
        res = s.get(url) if url else res

    return session(res.url.split('access_token=')[1].split('&')[0], s)
