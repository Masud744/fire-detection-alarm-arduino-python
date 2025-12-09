import serial
import pygame
import time

ser = serial.Serial('COM3', 9600)
  # ekhane tmr real COM port

pygame.mixer.init()
pygame.mixer.music.load("fire_alarm.mp3")

fire_playing = False

print("Waiting for fire signal...")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Received:", data)

        if data == "Maka bhosda aaaaaagggg!!!!!" and not fire_playing:
            print("🔥 Fire detected! Playing alarm...")
            pygame.mixer.music.play(-1)
            fire_playing = True

        elif data == "NOFIRE!!!!" and fire_playing:
            print("✅ Fire gone. Stopping alarm...")
            pygame.mixer.music.stop()
            fire_playing = False

    time.sleep(0.1)

