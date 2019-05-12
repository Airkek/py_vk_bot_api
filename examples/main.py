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


res = upload.messageDocument(filename='file.zip', peer_id=1) #загрузка документов для отправки в сообщениях
res = upload.audioMessage(filename='audio.mp3', peer_id=1) #загрузка аудиосообщений
res = upload.messagePhoto(filename='photo.png', peer_id=1) #загрузка фото для отправки в сообщениях

"Следующие методы можно вызвать только с пользовательским ключем доступа"
res = upload.albumPhoto(filename='photo.png', album_id=1, group_id=1) #загрузка фото в альбом
res = upload.wallPhoto(filename='photo.png', group_id=1, caption="Моё крутое фото") #загрузка фото для стены
res = upload.document(group_id=1) #загрузка документов


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
Вскоре даже через Kate Mobile нельзя будет, Users LongPoll делать смысла я не вижу
"""
