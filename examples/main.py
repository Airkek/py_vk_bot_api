import py_vk_bot_api as lib
TOKEN = "" #наш VK токен

session = lib.session(TOKEN)

"""
Использование методов API
"""
api = lib.api(session)
res = api.call("users.get", {'user_ids': 1})
#res == [{'first_name': 'Pavel', 'last_name': 'Durov', 'id': 1}]

"""
Загрузка документов на сервер VK
"""
upload = lib.upload(session)
res = upload.audioMessage('audio.mp3') #загрузка аудиосообщений
"Comming Soon..."

"""
Создание бота (группа)
"""
bot = lib.botsLongPoll(session)

@bot.on
def message_new(msg):
    if msg['text'] == "Hi": #если текст сообщения равен "Hi"
        msg['send']("Hello!") #отвечаем "Hello!"

bot.startPolling() #начинаем получать события с LongPoll


"""
Создание бота (пользователь)
"""

"""
Этого сделать больше нельзя (можно только если через токен Kate Mobile (получается через lib.userAuth))
Вскоре даже черех Kate Mobile нельзя будет, Users LongPoll делать смысла я не вижу
"""
