import datetime
import time
import asyncio
import subprocess

from function import send_suspended
from telegram_bot import send_admin_message

suspended = '🔴Page 5/17: Suspended'
while True:
    try:
        send_suspended(suspended)
    except Exception as ex:
        print('Try send suspended, Error:', ex)
        send_admin_message('🔴Exception block: Try send backup_suspended')
        time.sleep(5)
    # Chờ một khoảng thời gian trước khi thử lại (ví dụ: 10 giây)
    time.sleep(30)
