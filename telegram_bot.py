import requests
import json
import datetime
import pytz  # Import thư viện pytz để làm việc với múi giờ
import asyncio

from time import sleep
from telegram import Bot

api_telegram_TOKEN = '5848712014:AAHb0BppwOWo54aSp_rlOE8_uQkpJl01GRY'
vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')

async def send_to_telegram_suspended(text):
    #chat_id = '-1001915546898' #462_immi_autocall
    #chat_ids = ['-656277664', '-1001987376002',] #group 2, 462 immi bot bật thông báo
    chat_ids = ['-710009970'] #group premium

    now = datetime.datetime.now(vietnam_timezone)
    #date_str = now.strftime("%Y-%m-%d")
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    text_with_timestamp = f"{text}\n🔴{date_str} {time_str}"
    
    bot = Bot(token=api_telegram_TOKEN)
    for chat_id in chat_ids:
        message = await bot.send_message(chat_id=chat_id, text=text_with_timestamp, timeout=10)

#async def send_and_delete(text):
#    await send_to_telegram_suspended(text)

async def send_and_delete(text):
    #chat_id = '-1001915546898' #462_immi_autocall
    #chat_ids = ['-888905818'] #group test call
    chat_ids = ['-1001877646068'] #Bot_canh_462_immi_1m

    now = datetime.datetime.now()
    #date_str = now.strftime("%Y-%m-%d")
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    text_with_timestamp = f"{text}\n🔴{date_str} {time_str}"
    
    bot = Bot(token=api_telegram_TOKEN)
    for chat_id in chat_ids:
        message = await bot.send_message(chat_id=chat_id, text=text_with_timestamp, timeout=10)

    #Lấy ID của tin nhắn để xóa sau đó
    message_id = message.message_id
    await asyncio.sleep(1)
    for chat_id in chat_ids:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

async def send_admin_message(text):
    #chat_id = '-1001915546898' #462_immi_autocall
    #chat_ids = ['-656277664', '-1001987376002',] #group 2, 462 immi bot bật thông báo
    chat_ids = ['-1001986922268'] #group admin

    now = datetime.datetime.now(vietnam_timezone)
    #date_str = now.strftime("%Y-%m-%d")
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    text_with_timestamp = f"{text}\n🔴{date_str} {time_str}"
    
    bot = Bot(token=api_telegram_TOKEN)
    for chat_id in chat_ids:
        message = await bot.send_message(chat_id=chat_id, text=text_with_timestamp, timeout = 10)





