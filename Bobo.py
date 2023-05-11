import requests

import telegram



# create a Telegram bot instance

bot = telegram.Bot(token='5857821445:AAHrCIPNR2rbxB0b4g2iXsIbWn56DYkSy7c')



# specify the URL of the file to download

file_url = 'https://www.example.com/file.pdf'



# make a GET request to download the file

response = requests.get(file_url)



# create a file-like object from the response content

file_obj = response.content



# send the file to a Telegram chat

chat_id = 'https://t.me/Bokokoto_bot'

bot.send_document(chat_id=chat_id, document=file_obj)

