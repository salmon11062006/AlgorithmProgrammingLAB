todo_list = []
print("1. Add Tasks")
print('2. Remove Tasks')
print('3. Mark Tasks')
print('4. View Tasks')

def add_task(description):
    task = {
        'description': description,
        'completed': False
    }

    todo_list.append(task)
    print(f'Done! {description} has been added to your tasks!')

def remove_task(description):
    for task in todo_list:
        if task['description'] == description:
            todo_list.remove(task)
            print(f'Say goodbye to {description}')
            break

def mark_task(description):
    for task in todo_list:
        if task['description'] == description:
            task['completed'] = True
            print(f'Yay! You have {description}!')
            break

choice = eval(input("Enter your choice!: "))

if choice == 1:
    add_task(str(input("What's the task?: ")))
elif choice == 2:
    remove_task(str(input('What do you want to get rid of?: ')))
elif choice == 3:
    mark_task(str(input('What do you want to mark as done?: ')))

if choice == 4:
    print(todo_list)