import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        match text_data_json['type']:
            case "get_info":
                self.send(text_data=json.dumps({"message": "mucha info junta"}))

            case _:
                self.send(
                    text_data=json.dumps(
                        {"message": "estas preguntando cualquier gilada "}
                    )
                )
