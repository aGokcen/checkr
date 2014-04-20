import imaplib
from SiteLogin import SiteLogin


class GmailLogin(SiteLogin):

    gmail_url = "imap.gmail.com"

    def attempt_login(self, username, pwd):

        try:
            ssl_connection = imaplib.IMAP4_SSL(self.gmail_url)

        except:
            raise Exception

        try:
            ssl_connection.login(username, pwd)

        except:
            return False
        return True
