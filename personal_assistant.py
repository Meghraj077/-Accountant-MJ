import os
import json

TASKS_FILE = "tasks.json"

def add_task(task):
    """ नई Task को Save करें """
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)

    with open(TASKS_FILE, "r+") as file:
        tasks = json.load(file)
        tasks.append(task)
        file.seek(0)
        json.dump(tasks, file)

    return "Task Added!"

if __name__ == "__main__":
    task = input("Enter Task: ")
    print(add_task(task))
