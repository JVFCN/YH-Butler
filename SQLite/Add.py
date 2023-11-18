import sqlite3


def User(UserId, UserName):
    db = sqlite3.connect("data/UsersInfo.db")
    cursor = db.cursor()

    # 查询要插入的值是否已存在
    cursor.execute("SELECT COUNT(*) FROM Users WHERE UserId = ?", (UserId,))
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("INSERT INTO Users (UserId, UserName, MsgNum) VALUES (?, ?, 0)", (UserId, UserName))
        db.commit()

    db.close()


def MsgNum(UserId):
    db = sqlite3.connect("data/UsersInfo.db")
    cursor = db.cursor()

    cursor.execute("UPDATE Users SET MsgNum = MsgNum + 1 WHERE UserId = ?", (UserId,))
    db.commit()

    db.close()
