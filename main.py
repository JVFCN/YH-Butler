import os
import threading

from dotenv import load_dotenv
from flask import Flask, request
from yunhu.openapi import Openapi
from yunhu.subscription import Subscription

from SQLite import Daily, Add, Init

load_dotenv()
app = Flask(__name__)
sub = Subscription()
openapi = Openapi(os.getenv("TOKEN"))
Init.DB()
thread = threading.Thread(target=Daily.ScheduleThread)
thread.start()


@app.route('/sub', methods=['POST'])
def subRoute():
    if request.method == 'POST':
        sub.listen(request)
        return "success"


@sub.onMessageNormal
def onMessageNormalHander(event):
    # print(event)
    if event["chat"]["chatType"] == "group" and event["chat"]["chatId"] == os.getenv("CHAT_ID"):
        SenderId = event["sender"]["senderId"]
        SenderName = event["sender"]["senderNickname"]
        Add.User(SenderId, SenderName)
        Add.MsgNum(SenderId)


if __name__ == '__main__':
    app.run("0.0.0.0", 7725)
