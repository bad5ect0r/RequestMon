import requests


PUSHOVER_API_TOKEN = ''
PUSHOVER_URL = 'https://api.pushover.net/1/messages.json'
PUSHOVER_USER_KEY = ''
PUSHOVER_DEVICE = ''


def send_message(title, message):
    data = {
        'token': PUSHOVER_API_TOKEN,
        'user': PUSHOVER_USER_KEY,
        'title': title,
        'message': message,
    }

    return requests.post(PUSHOVER_URL, data=data)

