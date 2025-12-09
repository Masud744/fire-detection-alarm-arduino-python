# Fire Detection & Alarm System (Arduino + Python MP3 Alert)


This project is a simple but practical fire detection system that uses an **Arduino + flame sensor** to detect fire and a **Python script on a laptop** to play an MP3 alarm sound. An optional **I2C LCD (16×2)** can be added to show messages such as “System Ready”, “FIRE DETECTED!”, and “No Fire”.

The goal of this README is to give anyone enough information to **rebuild the full project from the files in this repo**, without needing to read the source code first.

---

## 1. Project Overview

You will build a system where:  

- The Arduino reads a **flame sensor (digital output)**  
- When fire is detected, the Arduino sends a message over **USB serial** to your laptop  
- A **Python script** on the laptop receives this message and plays an **alarm MP3 in a loop**  
- When the fire is no longer detected, the Arduino sends a different message and the Python script **stops the alarm**  
- *(Optional)* An I2C LCD on the Arduino shows clear status messages

This project is great for:
- Learning basic **IoT & embedded systems**
- Understanding **serial communication (Arduino ↔ PC)**
- Practicing **Python with hardware integration**

This README is based on the original manual included in this repo.  

---

## 2. Files in This Project

Recommended repository structure:

```text
FireAlarmProject/
│
├── fire_alarm.ino        # Arduino sketch (with or without LCD support)
├── fire_alarm.py         # Python script that plays the MP3 when fire is detected
├── fire_alarm.mp3        # Alarm sound file (any siren sound renamed to this)
├── manual.pdf            # Original detailed manual (PDF)
└── README.md             # This documentation file
```

> **Note:** You do not need to copy code from this README. All actual code lives in the `.ino` and `.py` files.

---

## 📹 Demo Video  
👉 https://www.youtube.com/shorts/zvIpvsSzm64  

---

## 3. Required Components

### 3.1 Hardware

- **Arduino UNO**
- **Flame Sensor Module** (with digital output pin `DO`)
- **Jumper Wires**
- **USB Cable** (Arduino to laptop/PC)
- *(Optional)* **I2C 16×2 LCD** module (for on-device messages)

These match the original manual description. fileciteturn1file0

### 3.2 Software

- **Arduino IDE** (for uploading the Arduino sketch)
- **Python 3.x** (3.10–3.12 recommended)
- Python packages:
  - `pyserial` (for serial communication)
  - `pygame` (for playing the MP3 alarm)

---

## 4. Hardware Connections

### 4.1 Flame Sensor → Arduino

Connect the flame sensor to the Arduino as follows: fileciteturn1file0

| Flame Sensor Pin | Arduino Pin |
|------------------|------------|
| VCC              | 5V         |
| GND              | GND        |
| DO (Digital Out) | D2         |

> **Important:** On many flame sensor modules, **DO = LOW** when fire is detected (active low). The Arduino code provided in `fire_alarm.ino` assumes this behavior.

### 4.2 Optional: I2C LCD → Arduino

If you want to use LCD status messages, connect the I2C LCD as described in the manual: fileciteturn1file0

| LCD Pin | Arduino Pin |
|---------|------------|
| GND     | GND        |
| VCC     | 5V         |
| SDA     | A4         |
| SCL     | A5         |

You will also need the **LiquidCrystal I2C** library (see Section 6.2).

---

## 5. Folder Setup on Your Laptop

Create a project folder (for example on Desktop or D: drive):

```text
D:\FireAlarmProject
```

Place the following files inside this folder:

- `fire_alarm.py`
- `fire_alarm.mp3`
- `fire_alarm.ino`

The Python script assumes that `fire_alarm.mp3` is in the **same folder**. fileciteturn1file0

---

## 6. Arduino Side Setup

### 6.1 Open and Upload the Sketch

1. Open **Arduino IDE**.  
2. Go to **File → Open** and select `fire_alarm.ino` from this project.  
3. Select your board and port:  
   - **Tools → Board → Arduino Uno**  
   - **Tools → Port → (select COMx where your Arduino is)**  
4. Click **Upload**.

After upload, if you are using the LCD version, you should see on the LCD: fileciteturn1file0  

- `System Ready` on startup  
- `FIRE DETECTED!` when fire is present  
- `No Fire` when fire is gone  

If you are using the no-LCD version, the messages will still be sent over serial for the Python script.

### 6.2 (Optional) Install the LCD Library

If using an I2C LCD, install **LiquidCrystal I2C** from the Arduino Library Manager: fileciteturn1file0  

1. In Arduino IDE: **Sketch → Include Library → Manage Libraries…**  
2. Search for: `LiquidCrystal I2C`  
3. Install a compatible version.

---

## 7. Python Environment Setup

### 7.1 Install Python

1. Download Python from the official website: fileciteturn1file0  
   - https://www.python.org/downloads/  
2. During installation, make sure to **check**:  
   - ✅ “Add Python to PATH”  
3. After installation, open **Command Prompt** and verify:

```bash
python --version
```

If it shows a version (e.g., `Python 3.12.7`), Python is installed correctly.

### 7.2 Install Python Libraries

Open Command Prompt and run: fileciteturn1file0

```bash
pip install pyserial pygame
```

This will install:
- `pyserial` → to talk to Arduino via COM port  
- `pygame` → to play the alarm MP3

---

## 8. Configure the Python Script

1. Find which COM port your Arduino is using:  
   - Open Arduino IDE → **Tools → Port** → note the `COMx` value (e.g., `COM3`).  
2. Open `fire_alarm.py` in a text editor (Notepad, VS Code, etc.).  
3. Locate the line that opens the serial port (it will look similar to): fileciteturn1file0  

   ```text
   ser = serial.Serial('COM3', 9600)
   ```

4. Change `'COM3'` to match your actual Arduino port if needed (e.g., `'COM4'`).  
5. Save the file.

The Python script listens for messages like `"FIRE"` and `"NOFIRE"` from the Arduino and controls the MP3 alarm based on these messages. fileciteturn1file0

---

## 9. Running the Full System

### 9.1 Close the Arduino Serial Monitor

Before running Python, make sure the Arduino Serial Monitor is **closed**. fileciteturn1file0  

> Only one program can use the COM port at a time. If Serial Monitor is open, Python will not be able to connect.

### 9.2 Start the Python Alarm Script

In Command Prompt, navigate to your project folder and run:

```bash
cd D:\FireAlarmProject
python fire_alarm.py
```

If everything is set up correctly, you should see in the console:

```text
Waiting for fire signal...
```

The script is now listening for serial messages from the Arduino.

### 9.3 Test with a Flame

Follow the manual’s test procedure: fileciteturn1file0  

1. Bring a lighter or small flame near the sensor (do not hold it too close for too long – be safe!).  
2. When fire is detected:  
   - Arduino sends `"FIRE"` over serial  
   - Python console shows `FIRE`  
   - The laptop plays `fire_alarm.mp3` (looping alarm)  
   - *(Optional)* LCD shows **“FIRE DETECTED!”**  
3. Move the flame away:  
   - Arduino sends `"NOFIRE"` over serial  
   - Python console shows `NOFIRE`  
   - The alarm sound stops  
   - *(Optional)* LCD shows **“No Fire”**  

If you see this behavior, your system is working correctly.

---

## 10. Common Issues & Troubleshooting

- **Python error: “could not open port 'COMx'”**  
  - Check that the correct COM port is set in `fire_alarm.py`.  
  - Make sure the Arduino is plugged in.  
  - Close the Arduino Serial Monitor before running Python.

- **Python script runs but no sound plays**  
  - Check that `fire_alarm.mp3` is in the same folder as `fire_alarm.py`. fileciteturn1file0  
  - Ensure your PC/laptop speakers are not muted.  
  - Verify that `pygame.mixer.init()` does not throw any errors.

- **No reaction when bringing flame near sensor**  
  - Double-check wiring: VCC → 5V, GND → GND, DO → D2. fileciteturn1file0  
  - Some flame sensors have an onboard potentiometer—try adjusting sensitivity.  
  - Confirm that the Arduino sketch is correctly uploaded to the board.

---

## 11. Extending the Project

Once you have the basic system working, you can extend it by:

- Adding **buzzer** or **LEDs** on the Arduino side  
- Sending fire alerts to the cloud or a **mobile app**  
- Logging fire events with timestamps in a log file using Python  
- Displaying a graphical dashboard showing system status

---

## 👨‍💻 12. Author

**Shahriar Alom Masud**  
B.Sc. in IoT & Robotics Engineering
University of Frontier Technology, Bangladesh
Passionate about **IoT, Robotics, AI and ML**

**Email:** shahriar0002@std.uftb.ac.bd  
**LinkedIn:** https://www.linkedin.com/in/shahriar-alom-masud  

> Feel free to open an Issue or Pull Request if you find a bug or want to improve this guide.
