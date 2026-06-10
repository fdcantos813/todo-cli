import json
import os

FILE = "todos.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add(task):
    todos = load()
    todos.append({"task": task, "done": False})
    save(todos)
    print(f"Added: {task}")

def list_todos():
    todos = load()
    if not todos:
        print("No todos yet!")
        return
    for i, t in enumerate(todos):
        status = "✓" if t["done"] else "○"
        print(f"{i+1}. [{status}] {t['task']}")

def complete(index):
    todos = load()
    todos[index - 1]["done"] = True
    save(todos)
    print(f"Completed: {todos[index - 1]['task']}")
    
def delete(index):
    todos = load()
    removed = todos.pop(index - 1)
    save(todos)
    print(f"Deleted: {removed['task']}")
    
def main():
    import sys
    args = sys.argv[1:]
    if not args:
        list_todos()
    elif args[0] == "add":
        add(" ".join(args[1:]))
    elif args[0] == "done":
        complete(int(args[1]))
    elif args[0] == "delete":
        delete(int(args[1]))
    else:
        print("Usage: python todo.py [add <task> | done <number> | delete <number>]")

if __name__ == "__main__":
    main()
