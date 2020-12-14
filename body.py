import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['math'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/cnd-unhv-sxj".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['phy'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/axp-fpuh-hya".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['phylb'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/qnn-qwvt-ufn".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['pro'])
def welcome(message):
    bot.send_message(message.chat.id, "meet.google.com/wkv-uadx-sjx".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['op'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/vfv-dtcs-pov".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['vvsp'])
def welcome(message):
    bot.send_message(message.chat.id, "http://meet.google.com/fhy-ocgi-oms".format(message.from_user, bot.get_me()),
    parse_mode='html')
@bot.message_handler(commands=['phylbch'])
def welcome(message):
    bot.send_message(message.chat.id, "https://meet.google.com/fog-duvj-mjp".format(message.from_user, bot.get_me()),
    parse_mode='html')


@bot.message_handler(commands=['tagall'])
def welcome(message):
    bot.send_message(message.chat.id, "@VladFedorkin \n @parirambururi \n @electrovagina \n @hitecu \n @YouCallMeDeath".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@pixelated_batya \n @violetviole \n @raritet04ka \n @WaitForMeForever \n @Ryd_14".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@Blackprincer \n @Kirill_Volobuev \n @Slava_Beton \n @sandorka \n @skribex1337".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@brake0force \n @w3nzr \n @bespontovbIypirozhok \n @Max_Reid \n @DanilKalmykov".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@bohdanbelmaz \n @tttreep \n @errrni0 \n @s1ava0 \n @nwah_outlander".format(message.from_user, bot.get_me()),
    parse_mode='html')
    bot.send_message(message.chat.id, "@Haooss".format(message.from_user, bot.get_me()),
    parse_mode='html')
    
@bot.message_handler(content_types=['text'])
def lalala(message):
    if("ссылку" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("ссылка" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("Ссылку" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("ссыль" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("Ссыль" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("ссылку?" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("ссылка?" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("Ссылку?" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("ссыль?" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")
    elif("Ссыль?" in message.text):
        bot.send_message(message.chat.id, "Блять, а я тут для чого? Нужна ссылка - воспользуйся мной!\nЕсли ты не просил ссылку, то скажи это моему разрабу")


bot.polling(none_stop=True)
