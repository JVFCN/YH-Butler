import os
import sqlite3
import time

import schedule
from flask import Flask
from yunhu.openapi import Openapi
from yunhu.subscription import Subscription

app = Flask(__name__)
sub = Subscription()
openapi = Openapi(os.getenv("TOKEN"))


def Task():
    db = sqlite3.connect("data/UsersInfo.db")
    cursor = db.cursor()

    select_query = '''
        SELECT UserName, MsgNum FROM Users ORDER BY MsgNum DESC LIMIT 10;
    '''
    cursor.execute(select_query)
    result = cursor.fetchall()
    Data = "🏵 今日活跃用户排行榜 🏵"
    for row in result:
        Data += f"\n{row[0]}   {row[1]}"
    openapi.sendMessage(os.getenv("CHAT_ID"), "group", "text", {"text": Data})
    update_query = '''
        UPDATE Users SET MsgNum = 0;
    '''
    cursor.execute(update_query)
    db.commit()
    db.close()


def ScheduleThread():
    schedule.every().day.at("00:00").do(Task)
    # schedule.every(10).seconds.do(Task)

    while True:
        schedule.run_pending()
        time.sleep(1)
