import telebot 
from config import token
from logic import Pokemon 
from logic import Wizard
from logic import Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
    

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())

if __name__ == '__main__':
    wizard = Wizard("username1",1,1)
    fighter = Fighter("username2",1,1)

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))

@bot.message_handler(commands=['feed'])
def feed_pok(message):
    if message.from_user.username in Pokemon.pokemons.keys():
         pok = Pokemon.pokemons[message.from_user.username]
         response = pok.feed()
         bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'У вас нет покемона!')


bot.infinity_polling(none_stop=True)

