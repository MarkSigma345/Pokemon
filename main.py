import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
    
@bot.message_handler(commands=['feed'])
def feed(message):
    
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        pokemon.level_up()  # Вызываем метод для повышения уровня
        bot.send_message(message.chat.id, f"Ты покормил покемона!  Теперь его уровень: {pokemon.level}") # Отправляем сообщение об уровне
    else:
        bot.reply_to(message, "У тебя еще нет покемона! Используй /go чтобы создать.")
    

bot.infinity_polling(none_stop=True)

