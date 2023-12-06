import json

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []
        return tasks


    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = " [X]" if task['completed'] else " [ ]"
                print(f"{i}. {task['description']}{status}")

    def add_task(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            self.save_tasks()
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task {task_index} removed: {removed_task['description']}")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            todo_list.add_task(description)
            todo_list.display_tasks()
        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == '4':
            todo_list.display_tasks()
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
