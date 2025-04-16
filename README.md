# 🤖 Robotic Arm Control using WebSockets and Arduino Nano

This project allows you to **control a 3-DOF robotic arm** using a Python-based GUI client via WebSocket communication. The angles for the three servo motors are sent from a Python app to an Arduino Nano over serial.

## 🚀 Features

- Control 3 servo motors with precision
- Real-time CLI built using Python 
- WebSocket server handles data between GUI and Arduino
- Arduino Nano executes the servo movements
- Interactive, beginner-friendly setup

---

## 🧰 Tech Stack

- **Arduino Nano** (C++ with Arduino IDE)
- **Python 3** (asyncio, websockets, pyserial, tkinter)
- **Servo Motors** (SG90 or similar)

---

## 📁 Project Structure
├── server.py           # WebSocket server that sends data to Arduino
├── client.py       # Python CLI to control angles and send data
├── arduino code.ino     # Arduino code for receiving and moving servos
├── README.md

---

## 📝 How It Works

1. The **Python CLI** allows users to select angles for 3 servos using sliders.
2. The angles are sent to the **WebSocket server**.
3. The WebSocket server **sends the data via serial** to the Arduino Nano.
4. Arduino receives the angles and moves the **servo motors** accordingly.

---

## ✅ Requirements

- Python 3.11.10 or 9(Not 3.13)
- Arduino IDE
- Arduino Nano + 3x Servo Motors(you can use 4-5 servo motor for exta stability and smooth function).
- USB cable to connect Arduino Nano

---

## 📦 Python Dependencies

Install dependencies using pip:
1-pip install websockets pyserial

🔌 Arduino Setup
Connect your servos to pins 9, 10, 11 on the Nano.

Copy pastre arduino code to your Arduino Nano via Arduino IDE.
---

## 🖥️ Running the Project
1. Upload the Arduino code:
Select the correct board and port(I used Ardunio nano and COM5)
Upload the sketch.
After uploading close the Ardunio Ide.

2. Start the WebSocket server:
In Command prompt type;
python server.py or server.py

3. Run the CLI client:
In Command prompt type;
python client.py or client.py
Keep both command prompt open , dont close it.

You can change angles if needed.

🙋‍♀️ Author
Pooja Shinde
🔧 Electronics & Telecommunication Engineer
💡 IoT | Embedded | Robotics | Automation Enthusiast

⭐️ Give it a Star!
If you like this project, consider giving it a ⭐ on GitHub. It helps a lot! websockets pyserial
