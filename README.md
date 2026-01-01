# TCP-chat-room
A simple multi-client chat application built using Python socket programming and threading.
It supports public chat, private messaging, and a graceful exit option.

📌 Features

✅ Multiple clients can connect simultaneously

💬 Public (broadcast) chat

🔒 Private messaging using @username

👥 View online users with /users

🚪 Graceful exit using /exit or /quit

⚡ Real-time communication (TCP sockets)

🛠️ Technologies Used

Python 3

socket module

threading module

📂 Project Structure
chat-app/
│
├── server.py   # Server-side code
├── client.py   # Client-side code
└── README.md   # Project documentation

▶️ How to Run the Project
1️⃣ Start the Server
python server.py


You should see:

[START] Server running on 127.0.0.1:5559

2️⃣ Start Clients (Open multiple terminals)
python client.py


Enter a nickname when asked.

💡 How to Use
🔹 Public Message
hello everyone


➡️ Sent to all connected users

🔹 Private Message
@liza hi 


➡️ Sent only to liza

🔹 Show Online Users
/users

🔹 Exit Chat
/exit


or

/quit


➡️ Client disconnects safely and others are notified

🔐 Commands Summary
Command	Description
message	Public chat
@username message	Private message
/users	Show online users
/exit or /quit	Exit chat
⚠️ Notes

Server must be running before clients connect

All clients should use the same IP & port

Default:

IP: 127.0.0.1

Port: 5559

🎓 Learning Outcomes

This project helps you understand:

Client–Server architecture

TCP socket communication

Multithreading in Python

Real-time messaging systems

🚀 Future Improvements (Optional)

GUI version (Tkinter)

Message timestamps

File sharing

User authentication

Encryption (security)

👩‍💻 Author

Tasnima Akther Tisha
ID: 222-134-016
Fatheha Ahmed Liza 
ID: 231-134-025
