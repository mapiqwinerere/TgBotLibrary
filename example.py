#импорт библиотеки
import trying as l

#написание токенов(выполнить 1 раз, иначе документ будет содержать повторяющиеся строки)
l.write_token('botik', "ваш токен")#1-ым аргументом - название бота(любое), токен(полученный от BotFather)
l.write_token('bot', "ваш 2 токен")#можно создать несколько ботов

#создание телеграмм бота
tg = l.TgBot('botik')#передаём нужное нам название бота, записанное выше

#функции
def test_func(message):
    tg.message('Test!', message)#отправка сообщения

def player1(message):
    tg.message('player1 good player', message)

def player2(message):
    tg.message('player2 cool player', message)

def mom(message):
    tg.message('mom is mom', message)
    print("mom")

def dad(message):
    tg.message('dad is member of family', message)

def com1(message):
   tg.message('Write text', message)
   tg.next_step(com2, message)#назначение функции для последующего выполнения

def com2(message): #функция для последующего выполнения
    tg.message(str(message.text), message)#отправляет текст полученный от пользователя


buttons = ['player1', 'player2', 'mom', 'dad', 'com']# спсок с названиями кнопок(будут отброажаться у пользователя)
values = [player1, player2, mom, dad, com1]#список с функциями для кнопок(записывается, в той паоследовательности, которой были перданы кнопки; функции пишутся без "")

#функция для клавиатуры
def keyboard(message):
    global test_kb 
    global count
    test_kb = l.Keyboard(buts=buttons,
                         values = values,
                         row_width=2,
                         name='keyboard1',
                         text='choose button',
                         send_or_not=True,
                         message = message,
                         bot=tg)

def push_def(message):
    tg.message('You press push!', message)

buttons2 = ['push']     
values2 = [push_def]

def keyboard2(message):
    global test_kb2
    test_kb2 = l.Keyboard(buts=buttons2,
                         values = values2,
                         row_width=2,
                         name='keyboard2',
                         text='choose button please',
                         send_or_not=True,
                         message = message,
                         bot=tg)

#функция отправки test_kb(название перемнной клавиатуры, НЕ НАЗВАНИЕ, переданное в аргументах)
def send(message):
    test_kb.send()#пример использования .send()

#функция отправки keyboard2(название, переданное в аргументах)
def send2(message):
    l.send_keyboard('keyboard2')#пример использования send_keyboard()

#hadlers
tg.keyboard_hadler('kb2', keyboard2, "keyboard2")
tg.keyboard_hadler('kb', keyboard, 'keyboard1')
tg.hadlers('start', test_func)
tg.hadler('send', send)
tg.hadler('send2', send2)

#обязательно заупстить бота
tg.start()
