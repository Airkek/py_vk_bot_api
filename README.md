# Python vk.com API wrapper

Модуль для использования vk.com API в Python 3.6+

# Возможности

- [x] Использование VK API
- [x] Вход по логину и паролю
- [x] Использование Bots LongPoll
- [x] Загрузка голосовых сообщений
- [x] Загрузка фото
- [x] Загрузка документов

# Установка

```console
pip install py-vk-bot-api
```

# Исользование

```python
import py_vk_bot_api
session = py_vk_bot_api.session(access_token) #авторизация по токену
session = py_vk_bot_api.userAuth(login, password) #авторизация по л:п, реализовано не до конца
api = py_vk_bot_api.api(session)
api.call("users.get", {"user_ids": 1}) #[{'first_name': 'Pavel', 'last_name': 'Durov', 'id': 1}]
```

# [Примеры](https://github.com/Airkek/py_vk_bot_api/tree/master/examples)

## Полная документация по методам vk.com API - https://vk.com/dev/methods
