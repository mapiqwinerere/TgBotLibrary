#library tg_bot for github
import telebot
from telebot import types


keyboards_names = {}
counts = {}
keyboards_types = {}
buts_value = {}
counts_of_kyboards = {}

def write_token(bot, token):
    with open('tokens.txt', 'a') as file:        #открытие файла для записи токена
       text_for_write = bot + ' ' + token + "\n" #создания текста
       file.write(text_for_write)                #запись текста
       file.close()

def send_keyboard(keyboard):
    global keyboards_types
    args_for_markup = keyboards_types.get(keyboard) #получение информации о клавиатуре
    args_for_markup[0].bot.send_message(args_for_markup[1].chat.id,
                                    text = args_for_markup[2].format(args_for_markup[1].from_user),
                                    reply_markup=args_for_markup[3])    #её отправка
    

class Keyboard():
   def __init__(self, name, row_width, buts, values, text, send_or_not, message, bot):
      global buts_value
      global keyboards_names
      global keyboards_types
      global counts_of_kyboards
      global keyboards
          
      #параметры для класса Keyboard    
      self.name = name
      self.row_width = row_width
      self.buts = buts
      self.value = values
      self.text = text
      self.send_or_not = send_or_not
      self.message = message
      self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= row_width)
      self.bot = bot
      self.len_buts = 0
      self.len_values = 0
      self.count = 0
    
      keyboards_names[name] = {}
      keyboards_types[name] = [bot, message, text, self.keyboard] #создание ключа со значением, в котором хранится информация о клавиатуре(используется для функции "send_keyboard")
      counts_of_kyboards[name] = 0
      bot.markups.append(str(name)) #добавление клавиатуры в список клавиатур бота

      if self.len_buts == 0:       #проверка количество кнопок, для избежания их повторного создания
         for but in self.buts:
            bot.buts.append(but)   #добавление кнопок в список кнопок бота
            keyboards_names[name]['but_' + str(but)] = types.KeyboardButton(text = str(but))  #присвоение значений к кнопкам клавиатуры
         self.len_buts += 1

      if self.len_values == 0:        #проверка количество значений(функций), для избежания их повторного создания
         for value in self.value:
            bot.values.append(value)  #добавление значений в список значений бота
         self.len_values += 1

      for i in range(len(self.buts)):
          buts_value[buts[i]] = self.value[i] #присвоение значений кнопкам

      self.keyboard.add(*list(keyboards_names[name].values())) #добавление кнопок в клавиатуру
      if self.send_or_not and self.count == 0: #проверка нужно ли отправлять клавиатуру
         self.send()                           #отправка клавиатуры
         self.count += 1   

   def send(self):  #функция отправки клавиатуры
         self.bot.bot.send_message(self.message.chat.id,
                                   text = self.text.format(self.message.from_user),
                                   reply_markup=self.keyboard)
       
class TgBot():
    def __init__(self, name_bot): 
        global bot
        global token

        bots_list = []
        bots_dict = {}

        with open('tokens.txt', 'r') as file:            #получение токена бота
            start_text = file.read()                     #прочтение файла
            split_text = list(start_text.split())        #разделение текста
            count = 0
            for i in range(len(split_text)):
                if count == 0:
                   bots_list.append(str(split_text[0]))  #добавление бота в список

                elif count == 1:
                   bots_dict[str(split_text[0])] = str(split_text[1]) #создания ключа значения(имя бота/токен)
                count += 1

        for bot in bots_list:   #поиск нужного токена(бота)
            if name_bot == bot:
               self.bot = telebot.TeleBot(bots_dict[name_bot]) #создание бота

        #параметры класса TgBot
        self.buts = []
        self.values = []
        self.markups = []
    
    #функция определения hadler`ов(по опеределённому слову выполняется заданная функция)
    def check_function(self):
       @self.bot.message_handler(content_types='text')
       def check_2(message):
          global buts_value
          for but in self.buts:
             if(message.text == but):
                buts_value.get(but)(message) #получение значений(функций)

    def start(self):
       self.check_function()  #запуск проверки hadler`ов
       self.bot.polling()     #запуск бота
       
    def message(self, text, message):
        self.bot.send_message(message.chat.id, text)
 
    def hadlers(self, *args):
       global command
       global counts_of_kyboards
    
       if len(args) == 2:   #обычные hadler`ы
          @self.bot.message_handler(commands=[args[0]])
          def command(message):
              args[1](message)

       elif len(args) >= 3:   #hadler`ы для клавиатур
          counts[args[0]] = 0
          @self.bot.message_handler(commands=[args[0]])
          def command(message):
              if counts[args[0]] == 0: #если клавиатура отправляется в 1-ый раз
                 args[1](message)
                 counts[args[0]] += 1
              else:   #если клавиатура отправляется не в 1-ый раз
                 send_keyboard(args[2])
       else:
          print('Maybe you make mistacke in your code. Please check it.')
                     
    #функция создания hadler`ов     
    def hadler(self, word, function): 
       global command
       
       @self.bot.message_handler(commands=[word])
       def command(message):
           function(message)
    
    #функция создания hadler`ов для клавиатуры
    def keyboard_hadler(self, word, func, keyboard):
       global command
       global counts

       counts[word] = 0
       @self.bot.message_handler(commands=[word])
       def command(message):
           if counts[word] == 0: #если клавиатура отправляется в 1-ый раз
              func(message)
              counts[word] += 1
           else:    #если клавиатура отправляется не в 1-ый раз
              send_keyboard(keyboard)
              
    def next_step(self, func, message):
         self.bot.register_next_step_handler(message=message, callback=func)
