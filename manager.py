from fastapi.websockets import WebSocket
from datetime import datetime


class WebSocketManager:
    def __init__(self):
        self.connected_clients = []

    async def connect(self, websocket: WebSocket):
        client_ip = f"{websocket.client.host}:{websocket.client.port}"


        # client has connected
        await websocket.accept()


        # add client to list of connected clients
        self.connected_clients.append(websocket)


        # send welcome message to the client
        message = {"client":client_ip,"message": f"Welcome {client_ip}"}

        await websocket.send_json(message)


    async def send_message(self, websocket: WebSocket, message: dict):

        message = {
            "client": message['client'],
            "message": message['content'],
            "timestamp":message['timestamp']
        }

        await websocket.send_json(message)

    async def disconnect(self, websocket):
        self.connected_clients.remove(websocket)
