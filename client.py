import socket
import threading
from datetime import datetime
import sys

print("Client starting...")

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 5559))
    print("Connected to server")
except Exception as e:
    print("Connection failed:", e)
    sys.exit()

running = True

# ================== Receive messages ==================
def receive():
    global running
    while running:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            if running:
                print("[ERROR] Connection lost!")
            break

# ================== Send messages ==================
def write():
    global running
    while running:
        try:
            msg = input("")
            if msg.lower() in ["/exit", "/quit"]:
                try:
                    client.send(msg.encode('ascii'))  # server notify
                except:
                    pass
                running = False
                print("[INFO] You left the chat.")
                client.close()
                break
            else:
                client.send(msg.encode('ascii'))
        except:
            if running:
                print("[ERROR] Failed to send message")
            break

# ================== Start threads ==================
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()