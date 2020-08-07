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
            state, str(id_chat)
        ]
    )
    connect.commit()
    return 1


def get_current_state(chat_id):
    """
    function to get the current state from db
    :param chat_id: id to get the required user state
    :param sql: query sql to get state
    :return: if there is no error return the current state if there is an error return the default state (1 or 1a)
    """
    connect = checking_db_connection()
    if not connect:
        return 0
    cursor = connect.cursor()
    try:
        cursor.execute(config.Query.select_state.value, [str(chat_id)])
        return cursor.fetchall()[0][0]
    except KeyError:
        return config.StateUser.S_START.value


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
    cursor.execute(sql_select, [str(message.chat.id)])
    if not cursor.fetchall():
        cursor.execute(
            sql_insert, [
                str(message.chat.id),
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name
            ]
        )
        connect.commit()
        return 1
    return 2


def add_new_request_name(message):
    connect = checking_db_connection()
    if not connect:
        return 0
    cursor = connect.cursor()
    cursor.execute(config.Query.select_user.value, [str(message.chat.id)])
    id_user = cursor.fetchall()[0][0]
    cursor.execute(
        config.Query.add_name_request.value, [
            message.text,
            id_user
        ]
    )
    connect.commit()
    return 1


def update_info_request(message, sql):
    connect = checking_db_connection()
    if not connect:
        return 0
    cursor = connect.cursor()
    cursor.execute(config.Query.select_user.value, [str(message.chat.id)])
    id_user = cursor.fetchall()[0][0]
    cursor.execute(
        sql, [
            id_user, message.text
        ]
    )
    connect.commit()
    return 1
