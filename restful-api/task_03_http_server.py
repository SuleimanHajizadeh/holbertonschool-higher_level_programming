#!/usr/bin/python3
"""
task_03_http_server.py

Sadə HTTP server yaradır. GET sorğularını qəbul edir və JSON cavab qaytarır.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """GET sorğularını emal edir"""
        # Cavab statusu və başlıqları
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # JSON cavab
        response = {"message": "Salam, HTTP server işləyir!"}
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """Serveri localhost:8080 ünvanında işə salır"""
    server_address = ('', 8080)  # '' → bütün interfeyslərdən gələn sorğular
    httpd = server_class(server_address, handler_class)
    print("Server işə düşdü, CTRL+C ilə dayandırın...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
