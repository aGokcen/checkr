from GmailLogin import login as gmail_login
from YahooLogin import login as yahoo_login
from HotmailLogin import login as hotmail_login

providers = {
    'gmail': {'displayName': 'GMail', 'icon': '/static/gmail.png', 'login': gmail_login},
    'yahoo': {'displayName': 'Yahoo!', 'icon': '/static/yahoo.png', 'login': yahoo_login},
    'hotmail': {'displayName': 'Hotmail', 'icon': '/static/hotmail.png', 'login': hotmail_login}
}
