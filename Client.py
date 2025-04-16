import asyncio
import websockets
import time

async def robotic_arm_sequence():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        print("🤖 Connected to Robot Arm WebSocket")

        # Step 1: Move to PICK position
        pick_angles = [0, 100, 70]
        pick_str = ",".join(map(str, pick_angles))
        print(f"📤 Moving to PICK position: {pick_str}")
        await websocket.send(pick_str)
        response = await websocket.recv()
        print(f"📩 Server: {response}")

        # Simulate gripping delay
        time.sleep(5)

        # Step 2: Move to DROP position
        drop_angles = [90, 0, 180]
        drop_str = ",".join(map(str, drop_angles))
        print(f"📤 Moving to DROP position: {drop_str}")
        await websocket.send(drop_str)
        response = await websocket.recv()
        print(f"📩 Server: {response}")

        # Simulate release delay
        time.sleep(1)

        print("✅ Pick and Place Complete!")

if __name__ == "__main__":
    asyncio.run(robotic_arm_sequence())
