import socket
import threading

host = '127.0.0.1'
port = 5559

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Broadcast function 
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass  # Ignore failed sends

#  Private message 
def private_message(sender, receiver_name, message):
    if receiver_name in nicknames:
        index = nicknames.index(receiver_name)
        clients[index].send(message)
    else:
        sender.send("User not found!".encode('ascii'))

#  Handle a client 
def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            # Graceful exit
            if message.lower() in ["/exit", "/quit"]:
                if client in clients:
                    index = clients.index(client)
                    nickname = nicknames[index]
                    clients.remove(client)
                    nicknames.remove(nickname)
                    client.send("You left the chat.".encode('ascii'))
                    client.close()
                    broadcast(f"[INFO] {nickname} has left the chat.".encode('ascii'))
                    print(f"[LEAVE] {nickname} disconnected gracefully.")
                break

            # Show online users
            elif message == "/users":
                users = "Online users: " + ", ".join(nicknames)
                client.send(users.encode('ascii'))

            # Private message
            elif message.startswith("@"):
                try:
                    name, msg = message.split(" ", 1)
                    receiver = name[1:]  # remove @
                    sender_nickname = nicknames[clients.index(client)]
                    private_message(client, receiver, f"[PM] {sender_nickname}: {msg}".encode('ascii'))
                    continue  # prevent broadcast to everyone
                except:
                    client.send("Invalid private message format. Use @username message".encode('ascii'))
                    continue

            # Broadcast to all clients
            else:
                sender_nickname = nicknames[clients.index(client)]
                broadcast(f"[CHAT] {sender_nickname}: {message}".encode('ascii'))

        except Exception as e:
            # Unexpected disconnect
            if client in clients:
                index = clients.index(client)
                nickname = nicknames[index]
                clients.remove(client)
                nicknames.remove(nickname)
                client.close()
                broadcast(f"[INFO] {nickname} disconnected unexpectedly.".encode('ascii'))
                print(f"[ERROR] {nickname} disconnected unexpectedly: {e}")
            break

#  Receive connections 
def receive():
    print(f"[START] Server started on {host}:{port}")
    print("[INFO] Waiting for clients...\n")

    while True:
        try:
            client, address = server.accept()
            print(f"[CONNECT] Connected with {address}")

            client.send("NICK".encode('ascii'))
            nickname = client.recv(1024).decode('ascii')

            nicknames.append(nickname)
            clients.append(client)

            print(f"[INFO] Nickname set: {nickname}")
            broadcast(f"[INFO] {nickname} joined the chat!".encode('ascii'))
            client.send("Connected to the server! Type /quit or /exit to leave.".encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

        except Exception as e:
            print(f"[ERROR] Failed to accept connection: {e}")


receive()
