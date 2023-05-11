günlüğü içe aktar

telegram.ext içe aktarma Güncelleyicisi, CommandHandler'dan

içe aktarma istekleri



# URL yükleme işlevini tanımlayın

def upload_url(bot, güncelleme):

    metin = update.message.text

    url = text[8:] # "/upload " önekini kaldır

    # URL'yi bir bulut depolama hizmetine yükleyin (örn. Google Drive)

    # Ardından, Telegram Bot API'sini kullanarak dosya bağlantısını kullanıcıya gönderin

    bot.send_message(chat_id=update.message.chat_id, text="URL yüklendi.\nDosya bağlantısı: <file_link>")



# Telegram Bot API'sini kurun

güncelleyici = Güncelleyici(token='5857821445:AAHrCIPNR2rbxB0b4g2iXsIbWn56DYkSy7c')

gönderici = updater.dispatcher



# "/upload" komutu için bir komut işleyici ekleyin

upload_handler = CommandHandler('yükle', upload_url)

dispeçer.add_handler(upload_handler)



# Botu başlat

updater.start_polling()

