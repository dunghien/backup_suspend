import requests
import time
import asyncio
import subprocess

#from telegram_bot import send_and_pin_message
from telegram_bot import send_and_delete
from telegram_bot import send_to_telegram_suspended
from time import sleep
from random import randint

suspended = '🔴Page 4/16: Suspended'
opening = '🟢IMMI OPENING🟢. Submit now!!!'

def send_suspended(suspended):

    while True:
        start_time = time.time()
        '''
        # Khởi tạo event loop
        loop = asyncio.get_event_loop()
        sleep(1.5)

        # Chạy coroutine trong event loop
        loop.run_until_complete(send_and_delete('suspended'))
        '''
        asyncio.run(send_to_telegram_suspended(suspended))

        while True:
            '''
            loop = asyncio.get_event_loop()
            sleep(0.5)

            # Chạy coroutine trong event loop
            loop.run_until_complete(send_and_delete(suspended))
            '''
            start_time_2 = time.time()
            asyncio.run(send_and_delete(suspended))

            while True:
                x = randint(3,13)
                print('So s de auto click: {}'.format(x))
                sleep(1.5*x)
                elapsed_time_2 = time.time() - start_time_2
                print("elapsed_time:{0}".format(elapsed_time_2) + " [sec]")
                if elapsed_time_2 > 60:
                    print('1 minutes of notice and delete. Continue!')
                    break
            elapsed_time = time.time() - start_time
            if elapsed_time > 590:
                print('In last 10 minute. Continue')
                break
        print("elapsed_time_2:{0}".format(elapsed_time_2) + " [sec]")
        print("In last 10 minute: Immi not open")  



