import requests

def fetch_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")  # Cavabın status kodunu göstərir

    if response.status_code == 200:
        todo = response.json()  # JSON-u Python lüğətinə çevirir
        print("ID:", todo['id'])
        print("UserID:", todo['userId'])
        print("Title:", todo['title'])
        print("Completed:", todo['completed'])

fetch_todo()
