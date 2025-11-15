#!/usr/bin/env python3
import threading
import time
from task_04_net import start_server, send_data

def main():
    # Serveri ayrı thread-də başlatmaq
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Serverin işləməyə başlaması üçün 1 saniyə gözləmək
    time.sleep(1)

    # Client-dən məlumat göndərmək
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    # Server thread-in bitməsini təmin etmək
    server_thread.join()

if __name__ == "__main__":
    main()
