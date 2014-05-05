from GmailLogin import login as gmail_login
from YahooLogin import login as yahoo_login
from HotmailLogin import login as hotmail_login

providers = {
    'gmail': {'displayName': 'GMail', 'icon': '/img/gmail.png', 'login': gmail_login},
    'yahoo': {'displayName': 'Yahoo!', 'icon': '/img/yahoo.png', 'login': yahoo_login},
    'hotmail': {'displayName': 'Hotmail', 'icon': '/img/hotmail.png', 'login': hotmail_login}
}
