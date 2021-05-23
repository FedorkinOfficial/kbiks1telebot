import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['math'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/ubv-xkca-poq".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['otk'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/efi-oyqm-ioo".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['tekpz'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/eyu-cpkt-wfs".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['ufm'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/tzd-kqud-cyp".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['ver'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/qna-sgdx-ngr".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['prolk'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/ipi-agnn-yew".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['propz'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/yqe-khrq-kmr".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['bzd'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/urd-qptz-tsc".format(message.from_user, bot.get_me()),
    parse_mode='html')


@bot.message_handler(commands=['tagall'])
def welcome(message):
    bot.send_message(message.chat.id, "@VladFedorkin \n @onethousxndminusseven \n @electrovagina \n @hitecu \n @K_Tsukishima".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@pixelated_batya \n @violetviole \n @raritet04ka \n @Malakhova_Anna \n @Ryd_14".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@Blackprincer \n @Kirill_Volobuev \n @Slava_Beton \n @sandorka \n @skribex1337".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@brake0force \n @w3nzr \n @bespontovbIypirozhok \n @Max_Reid \n @DanilKalmykov".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@bohdanbelmaz \n @tttreep \n @errrni0 \n @nwah_outlander".format(message.from_user, bot.get_me()),
    parse_mode='html')
    
@bot.message_handler(commands=['thank'])
def welcome(message):
    bot.send_message(message.chat.id, "Спасибо @Malakhova_Anna от всей группы".format(message.from_user, bot.get_me()),
    parse_mode='html')

bot.polling(none_stop=True)
