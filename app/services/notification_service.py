from fastapi import WebSocket
from typing import Dict, List
import json
import asyncio
from app.core.config import settings
import redis

class NotificationService:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}
        self.redis_client = redis.from_url(settings.REDIS_URL)
        
    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)
        
    def disconnect(self, websocket: WebSocket, user_id: int):
        if user_id in self.active_connections:
            self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
                
    async def send_notification(self, user_id: int, message: dict):
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except Exception as e:
                    print(f"Error sending notification: {e}")
                    self.disconnect(connection, user_id)
                    
    async def broadcast_transaction(self, user_id: int, transaction_data: dict):
        message = {
            "type": "transaction",
            "data": transaction_data
        }
        await self.send_notification(user_id, message)
        
    async def broadcast_fraud_alert(self, user_id: int, alert_data: dict):
        message = {
            "type": "fraud_alert",
            "data": alert_data
        }
        await self.send_notification(user_id, message)
        
    async def broadcast_financial_advice(self, user_id: int, advice_data: dict):
        message = {
            "type": "financial_advice",
            "data": advice_data
        }
        await self.send_notification(user_id, message)
        
    def publish_to_redis(self, channel: str, message: dict):
        self.redis_client.publish(channel, json.dumps(message))
        
    async def subscribe_to_redis(self, channel: str):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        while True:
            message = pubsub.get_message()
            if message and message["type"] == "message":
                data = json.loads(message["data"])
                user_id = data.get("user_id")
                if user_id:
                    await self.send_notification(user_id, data)
            await asyncio.sleep(0.1)

notification_service = NotificationService() 