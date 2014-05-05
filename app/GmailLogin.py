import imaplib


def login(username, pwd):
    gmail_url = 'imap.gmail.com'
    try:
        ssl_connection = imaplib.IMAP4_SSL(gmail_url)

    except:
        return "Couldn't establish secure connection to Gmail!"

    try:
        ssl_connection.login(username, pwd)

    except:
        return False
    return True
