import asyncio
import websockets
import serial

# Update this with your actual COM port
arduino = serial.Serial('COM5', 9600, timeout=1)

async def handle_robotic_arm(websocket):
    print("🤖 Robotic Arm Server Ready")

    while True:
        try:
            angle_data = await websocket.recv()
            print(f"📥 Received angles: {angle_data}")

            # Send angle data to Arduino
            arduino.write(f"{angle_data}\n".encode())

            # Optional: Read confirmation from Arduino (if implemented)
            # response = arduino.readline().decode().strip()

            await websocket.send(f"✅ Angles sent: {angle_data}")

        except Exception as e:
            print(f"❌ Server Error: {e}")
            break

async def main():
    async with websockets.serve(handle_robotic_arm, "localhost", 8765):
        print("🔌 Server started at ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
