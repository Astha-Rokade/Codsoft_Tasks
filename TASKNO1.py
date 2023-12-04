class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the list.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found in the list.')

def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '4':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__== "_main_":
    main()