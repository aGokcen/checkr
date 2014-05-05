import imaplib


def login(username, pwd):
    hotmail = 'imap-mail.outlook.com'
    try:
        ssl_connection = imaplib.IMAP4_SSL(hotmail)

    except:
        return "Couldn't establish secure connection to Hotmail!"

    try:
        ssl_connection.login(username + '@hotmail.com', pwd)

    except:
        return False
    return True
