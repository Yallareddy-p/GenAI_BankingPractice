from fastapi import APIRouter, WebSocket, Depends, HTTPException
from app.services.notification_service import notification_service
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int,
    current_user: User = Depends(get_current_user)
):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
        
    await notification_service.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming messages if needed
            await websocket.send_json({"message": "Received"})
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        notification_service.disconnect(websocket, user_id) 