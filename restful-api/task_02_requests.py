#!/usr/bin/python3
"""
task_02_requests.py

JSONPlaceholder API-dən post-ları çəkir, çap edir və CSV faylına yazır.
"""

import requests
import csv


def fetch_and_print_posts():
    """Bütün post-ları çək və çap et (nümunə üçün bir post)"""
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"ID: {data['id']}")
        print(f"UserID: {data['userId']}")
        print(f"Title: {data['title']}")
        print(f"Completed: {data['completed']}")


def fetch_and_save_posts():
    """Bütün post-ları CSV faylına yaz"""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # CSV faylı yaratmaq
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["userId", "id", "title", "completed"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "userId": post["userId"],
                    "id": post["id"],
                    "title": post["title"],
                    "completed": post["completed"]
                })
