import imaplib


def login(username, pwd):
    yahoo = 'imap.mail.yahoo.com'
    try:
        ssl_connection = imaplib.IMAP4_SSL(yahoo)

    except:
        return "Couldn't establish secure connection to Yahoo! Mail"

    try:
        ssl_connection.login(username, pwd)

    except:
        return False
    return True
