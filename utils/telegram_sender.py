import requests

TOKEN = "8609694424:AAGfjIkBsvzd5vIHhRXZPvaa1YyUgrd74FA"
CHAT_ID = "8409741382"

def send_job(message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)