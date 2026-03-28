import argparse
import rich
from rich.table import Column, Table
from rich.console import Console

import json


def load_tasks(filepath):
  with open(filepath, 'r') as file:
    data = json.load(file)
  return data

tasks = load_tasks('todo.json')



def write_task(filepath, tasks):
    with open(filepath, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_name, description, duedate, priority):

    new_task = {
    "id": max([t["id"] for t in tasks], default=0) + 1,  
    "task": task_name,
    "description": description or "",
    "duedate": duedate or "",
    "priority": priority or "",
    "done": False
}

    tasks.append(new_task)
    write_task('todo.json', tasks)
    print("✅ Task Added")
    list_tasks()

def list_tasks():
    table = Table(title="Tasks List")
    table.add_column("ID")
    table.add_column("Task")
    table.add_column("Description")
    table.add_column("Due Date")
    table.add_column("Priority")
    for task in tasks:
        table.add_row(
            str(task.get("id", "")),
            str(task.get("task", "")),
            str(task.get("description", "")),
            str(task.get("duedate", "")),
            str(task.get("priority", ""))
        )

    console = Console()
    console.print(table)
    

def delete_task():
    pass

def search_task():
 pass


def main():


    parser = argparse.ArgumentParser(
                    prog='To Do CLI',
                    description='Track your tasks!',
                    epilog='<3')
    
    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser('add', help="add a new task")
    add_parser.add_argument('task', type=str, help="task name")
    add_parser.add_argument('--description', type=str, help="task description")
    add_parser.add_argument('--duedate', type=str, help="task due date")
    add_parser.add_argument('--priority', type=str, help="task priority")
    
    list_parser = subparsers.add_parser('list', help="list tasks")

    del_parser = subparsers.add_parser('delete', help="delete a task")
    del_parser.add_argument('task', type=str, help="Task to delete")

    search_parser = subparsers.add_parser('search', help="Search for tasks")
    search_parser.add_argument('task', type=str, help="Task to search for")
    

    args = parser.parse_args()

    if args.command == "add":
        add_task(tasks, args.task, args.description, args.duedate, args.priority)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delete_task(args.task)
    elif args.command == "search":
        search_task(args.task)




main()