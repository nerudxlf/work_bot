import sqlite3
import config


def checking_db_connection():
    """
    Checking the database connecting
    :return: 0 if failed connect to the database; connect to the database
    """
    try:
        connect = sqlite3.connect(config.DB)
        return connect
    except sqlite3.Error:
        return 0


def update_state(id_chat, sql, state):
    """
    Update the state in the db
    :param id_chat: user chat id (string)
    :param sql: query sql to update state
    :param state: the state itself (string)
    :return: 0 if error connecting to db; 1 if the state was updated in the db;
    """
    connect = checking_db_connection()
    if not connect:
        return 0
    cursor = connect.cursor()
    cursor.execute(
        sql, [
            state, id_chat
        ]
    )
    return 1


def adding_new_user(message, sql_insert, sql_select):
    """
    Adding a new user to the database if the user is not already in bd
    :param message: from bot
    :param sql_insert: sql query for adding new user to the db
    :param sql_select: sql query to get information on the user
    :return: 0 if error connecting to db; 1 if the user was added to the db; 2 if the user has already been added to the
    db
    """
    connect = checking_db_connection()
    if not connect:
        return 0
    cursor = connect.cursor()
    cursor.execute(sql_select, [message.chat.id])
    if not cursor.fetchall():
        cursor.execute(
            sql_insert, [
                message.chat.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name
            ]
        )
        connect.commit()
        return 1
    return 2
