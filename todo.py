import os

def display_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['description']}")

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    print("Task added!")

def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def save_tasks_to_file(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")

def load_tasks_from_file(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                description, completed_str = line.strip().split("|")
                tasks.append({"description": description, "completed": completed_str == "True"})
    return tasks

def main():
    tasks_filename = "tasks.txt"
    tasks = load_tasks_from_file(tasks_filename)

    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter task index to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == "4":
            save_tasks_to_file(tasks, tasks_filename)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
