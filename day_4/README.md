# To-Do List CLI Application

Welcome to the **To-Do List CLI Application**! This simple command-line tool helps you efficiently manage your tasks. Whether you're tackling assignments, managing goals, or simply keeping your life organized, this tool has you covered.

## Features
✅ Add new tasks  
✅ View current tasks with their status  
✅ Mark tasks as completed  
✅ Remove tasks from the list  
✅ User-friendly menu-based interface  
✅ Optional: Prioritize tasks (can be expanded as a future feature)

---

## How to Use

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd todo-list-cli
```

### Step 2: Run the Application
```bash
python todo_list.py
```

### Step 3: Choose an Option
You'll be presented with the following menu:
```
==== To - Do List =====
1. Add task
2. View Task
3. Remove task
4. Mark Task as done
5. Exit
```

### Step 4: Commands Overview
- **Add Task**: Enter a new task when prompted.
- **View Task**: Displays all tasks with their completion status.
- **Remove Task**: Enter the task number to remove it from the list.
- **Mark Task as Done**: Enter the task number to mark it as completed.
- **Exit**: Closes the application.

---

## Code Overview

### `add_task()`
```python
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")
```
*Adds a new task to the list.*

### `view_tasks()`
```python
def view_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")
```
*Displays all tasks with their status.*

### `remove_task()`
```python
def remove_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to remove: ")) - 1
    try:
        del tasks[task_number]
        print("Task removed!")
    except IndexError:
        print("Invalid task number.")
```
*Removes a specified task.*

### `mark_task_complete()`
```python
def mark_task_complete(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as done: ")) - 1
    try:
        tasks[task_number]["done"] = True
        print("Task marked as done!")
    except IndexError:
        print("Invalid task number.")
```
*Marks a specified task as completed.*

### `main()`
```python
def main():
    tasks = []

    while True:
        print("\n==== To - Do List =====")
        print("1. Add task")
        print("2. View Task")
        print("3. Remove task")
        print("4. Mark Task as done")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
*Main control flow of the application.*

---

## Example Usage
```
==== To - Do List =====
1. Add task
2. View Task
3. Remove task
4. Mark Task as done
5. Exit
Enter your choice: 1
Enter a new task: Python practice
Task added!

==== To - Do List =====
1. Add task
2. View Task
3. Remove task
4. Mark Task as done
5. Exit
Enter your choice: 4

Tasks:
1. Python practice - Not Done
Enter the task number to mark as done: 1
Task marked as done!
```

---

## Future Improvements
🚀 Add task prioritization  
🚀 Implement a save/load feature to keep tasks after exiting  
🚀 Add due dates and reminders  

---

## License
This project is open-source and available for personal or professional use. Contributions are welcome!

**Happy Coding!** 🎯


