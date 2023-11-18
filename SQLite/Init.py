import logging
import sqlite3


def DB():
    logging.info("Initializing SQLite database...")

    db = sqlite3.connect("data/UsersInfo.db")
    cursor = db.cursor()

    init_query = '''
        CREATE TABLE IF NOT EXISTS Users (
            UserId INTEGER PRIMARY KEY,
            UserName TEXT,
            MsgNum INTEGER
        );
    '''

    # 执行初始化查询
    try:
        cursor.execute(init_query)
        db.commit()
        logging.info("SQLite database initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing SQLite database: {e}")
    finally:
        db.close()