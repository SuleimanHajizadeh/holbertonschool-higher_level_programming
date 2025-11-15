#!/usr/bin/env python3
import socket
import json

# Server parametrləri
HOST = '127.0.0.1'  # localhost
PORT = 65432        # istənilən port

def start_server():
    """
    Serveri başlatmaq:
    - Client-dən gələn JSON məlumatını qəbul edir.
    - Deserialize edir və çap edir.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = s.accept()  # client bağlantısını qəbul edir
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)  # 1024 byte oxuyur
            if not data:
                return

            # JSON-dan Python dictionary-ə çevirmək
            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Received data is not valid JSON.")

def send_data(dictionary):
    """
    Client funksiyası:
    - Serverə dictionary göndərir (JSON formatında).
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Python dictionary → JSON string → bytes
            json_data = json.dumps(dictionary).encode('utf-8')
            s.sendall(json_data)
    except ConnectionRefusedError:
        print("Connection failed. Server may not be running.")
    except Exception as e:
        print(f"Client error: {e}")
