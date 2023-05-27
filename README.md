# description
Library TgBotMapi made for simplification writing code telegram bot. It includes functions - send messages, create and send markups, create command(handler), function assignments for keyboard buttons and assignment next function(register_next_step_handler).

# write_token 
Function save data about telegram bot(token and nick) in text document(tokens.txt). It acceptss arguments: bot(bot name) and token(received from BotFather).

# send_keyboard
Function send keyboard. It acceptss arguments: keyboard name, written you when you declare keyboard(with help from class Keyboard).

# Keyboard
Class creates markup. It acceptss arguments: name(markup name), row_width(number of buttons in ine string), buts(list with names of buttons), values(list with values for buttons), text(text, which send in the message), send_or_not(Bool-value(if True - send, False - do not send)), message(value of message, it for sending message), bot(bot(TgBot), in the chat which will be sent keyboard).

# send
Function of class Keyboard. Sent keyboard in the chat.

# TgBot
Class, which made telegram bot. It acceptss arguments: name_bot(name for bot).

# start
Function of class TgBot, which starts telegram bot and checking message on names of buttons(in keybpards).

# message
Function of class TgBot, which send message with text. Acccepts arguments: text(wich, will be sent in message) and message(value of message, it for sending message).

# hadlers
Function of class TgBot, which create command upon receipt of which start set function. It acceptss arguments(in a certain order): first - word, by which start function; second - function, which is activated  when a message is received; third - kayboard(if it is not specified, the functionality for the keyboard will not be presented, and therefore errors will occur).

# hadler
Function of class TgBot, which receivng, which executes the specified function. It acceptss arguments: word(by which start function) and function(which is activated  when a message is received).

# next_step
Function of class TgBot, which assigns function, which will be activated after the completion of the one in which it was written(use including for get answer from user and its further processing). It acceptss arguments: func(function) and message(value of message, it for sending message).

# Good luck!!!
