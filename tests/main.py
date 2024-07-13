import requests

API_URL = "http://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{API_URL}/users")
    response.raise_for_status()
    return response.json()

def get_todos():
    response = requests.get(f"{API_URL}/todos")
    response.raise_for_status()
    return response.json()

def is_fancode_city(user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    return -40 <= lat <= 5 and 5 <= lng <= 100

def get_completed_percentage(user_id, todos):
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_todos = [todo for todo in user_todos if todo['completed']]
    return len(completed_todos) / len(user_todos) * 100

def main():
    users = get_users()
    todos = get_todos()
    fancode_users = [user for user in users if is_fancode_city(user)]
    
    for user in fancode_users:
        completed_percentage = get_completed_percentage(user['id'], todos)
        print(f"User {user['name']} has completed {completed_percentage:.2f}% of their tasks.")
        if completed_percentage > 50:
            print(f"User {user['name']} has more than 50% tasks completed.")
        else:
            print(f"User {user['name']} has 50% or fewer tasks completed.")

if __name__ == "__main__":
    main()
