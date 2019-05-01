Python vk.com API wrapper
=========================

Это модуль для использования vk.com Api в Python (тестировалось только на 3.7)

Итак, начнём
==========

Установка
-------

```console
pip install requests
git clone https://github.com/Airkek/py_vk_bot_api/
cd py_vk_bot_api
python setup.py install
```

Исользование Api методов
-----

```python
import py_vk_bot_api
api = py_vk_bot_api.api(access_token)
api.call("users.get", {"user_ids": 1})

#output: [{'first_name': 'Pavel', 'last_name': 'Durov', 'id': 1}]
```

Полная документация по методам Api - https://vk.com/dev/methods

Использование Bots LongPoll Api
-----

```python
bot = py_vk_bot_api.botsLongPoll(api)

@bot.on
def message_new(msg):
    if msg['text'] == "Hi":
        msg['send']("Hello!") #ответить "Hello!"

bot.startPolling() #начинаем получать события с LongPoll

bot.stopPolling() #прекращаем получать события с LongPoll
```
