import json

from channels.generic.websocket import WebsocketConsumer
import requests
from decouple import config


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        match text_data_json["type"]:
            case "get_info":
                user = config("HTTP_API_USER")
                password = config("HTTP_API_PASSWORD")
                auth_tuple = (user, password)
                url = config("HTTP_API_URL")
                result = requests.get(url, auth=auth_tuple)
                self.send(text_data=json.dumps({"message": result.json()}))

            case _:
                self.send(
                    text_data=json.dumps(
                        {"message": "estas preguntando cualquier gilada "}
                    )
                )
