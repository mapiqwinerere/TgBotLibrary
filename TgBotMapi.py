#library tg_bot for github

#imports
import telebot
from telebot import types

#function for writing the data needed to create a bot to a text file
def write_token(bot, token):
    with open('tokens.txt', 'a') as file:
       text_for_write = bot + ' ' + token + "\n"
       file.write(text_for_write)
       file.close()

class Keyboard():
   def __init__(self, name, row_width, buts, value, text, send, message, bot):
      global buts_value
      global keyboards

      self.name = name
      self.row_width = row_width
      self.buts = buts
      self.value = value
      self.text = text
      self.send = send
      self.message = message
      self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= row_width)
      keyboards = {}
      keyboards[name] = {}
      
      for but in buts:
          keyboards[name]['but' + str(but)] = types.KeyboardButton(but)
          self.buts.append(but)
      
      for i in range(len(self.buts)):
          self.buts_value[self.buts[i]] = self.value[i]
   
      dictionary_values = list(self.keyboards[name_keyboard].values())
      keyboard.add(*dictionary_values)

      if self.send:
          self.keyboard.send(bot)

   def send(self, bot):
      bot.bot.send_message(self.message.chat.id, text = self.text_user.format(message.from_user), reply_markup=self.keyboard)

class TgBot():
    def __init__(self, name_bot): 
        global bot
        global keyboards
        global buts
        global buts_value

        bots_list = []
        bots_dict = {}

        with open('tokens.txt', 'r') as file:
            start_text = file.read()
            split_text = list(start_text.split())
            count = 0
            for line in range(len(split_text)):
                if count == 0:
                   bots_list.append(str(split_text[0]))

                elif count == 1:
                   bots_dict[str(split_text[0])] = str(split_text[1])
                count += 1

        for bot in bots_list:
            if name_bot == bot:
               token = bots_dict.get(name_bot)
            elif token == None:
                print("None")
        self.bot = telebot.TeleBot(token)
       
        self.keyboards = {}
        self.buts = []
        self.buts_value = {}

    #function to launch telegram bot
    def start(self):
       @self.bot.message_handler(content_types='text')
       def check_2(message):
            for but in self.buts:
               if(message.text == but):
                  self.buts_value.get(but)(message)
       self.bot.polling()
    
    #function to send messages
    def message(self, text, message):
        self.bot.send_message(message.chat.id, text)

    #function to create keyboards    
    def keyboard(self, buts, values, name_keyboard, row_width, text_user, send, message):
       global buts_value

       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= row_width)
       self.keyboards[name_keyboard] = {}
       
       #add buttons
       for but in buts:
           self.keyboards[name_keyboard]['but' + str(but)] = types.KeyboardButton(but)
           self.buts.append(but)
       
       #assignment function for buttons
       for i in range(len(buts)):
           self.buts_value[buts[i]] = values[i]
           self.values = values
      
       dictionary_values = list(self.keyboards[name_keyboard].values())
       keyboard.add(*dictionary_values)
       
       #send keyboard if send = True
       if send:
           self.bot.send_message(message.chat.id, text = text_user.format(message.from_user), reply_markup=keyboard)
    
    #function to create hadler
 
    def keyboard(self, name_keyboard, row_width, buts, value, text, send, message):
        self.keyboards[name_keyboard] = Keyboard(name_keyboard, row_width, buts, value, text, send, message)
       
    def hadler(self, word, user_function):
       global command
       
       @self.bot.message_handler(commands=[word])
       def command(message):
           user_function(message)
        
    #function to create a second function when the first one finishes
    def next_step(self, func, message):
         self.bot.register_next_step_handler(message=message, callback=func)
