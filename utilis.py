import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(text):
    try:
        url = "https://messages-sandbox.nexmo.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        auth = ("bc8651bc", "UhWBZrgmktUB8Gux")

        payload = {
            "from": "14157386102",
            "to": "2347032857263",
            "message_type": "text",
            "text": text,
            "channel": "whatsapp"
        }

        response = requests.post(url, headers=headers, auth=auth, json=payload)
        logger.info("Message sent")
    except Exception as e:
        logger.error("Error sending message")

