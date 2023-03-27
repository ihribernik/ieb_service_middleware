import asyncio
import json

import requests
from channels.generic.websocket import AsyncWebsocketConsumer
from decouple import config


class ProductConsumer(AsyncWebsocketConsumer):
    start = False
    current_id = ""
    user = config("HTTP_API_USER")
    password = config("HTTP_API_PASSWORD")
    url = config("HTTP_API_URL")

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        match text_data_json["type"]:
            case "get_info":
                action = text_data_json["action"]
                self.current_id = text_data_json["id"]
                if action == "start":
                    self.start = True
                else:
                    self.start = False

                await self._main_loop()
            case _:
                self.start = False
                await self.send(
                    text_data=json.dumps(
                        {"message": "estas preguntando cualquier gilada "}
                    )
                )

    async def _main_loop(self):
        while True:
            if self.start is True:
                auth_tuple = (self.user, self.password)
                if self.current_id:
                    self.url = f"{self.url}/{self.current_id}"

                result = requests.get(self.url, auth=auth_tuple)

                await self.send(
                    text_data=json.dumps({"message": result.json(), "status": "start"})
                )

            else:
                await self.send(text_data=json.dumps({"message": [], "status": "stop"}))
            await asyncio.sleep(10)
