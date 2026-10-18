import asyncio
from connection import create_table
from service import create_task, get_tasks, delete_task


async def main():
    await create_table()

    while True:

        n = input("1)Create task\n2)Get tasks\n3)Delete task\n0)Exit\nChoose one: ")

        match n:
            case "1":
                title = input("Enter task title: ").strip()

                if title:
                    await create_task(title)
                else:
                    print("Title cannot be empty")

            case "2":
                tasks = await get_tasks()

                for task in tasks:
                    print(f"""
Task ID: {task["task_id"]}
Title: {task["title"]}
Is active: {task["is_active"]}
Created at: {task["created_at"]}
""")

                if not tasks:
                    print("No tasks found")

            case "3":
                try:
                    task_id = int(input("Enter task ID: "))
                    await delete_task(task_id)
                except ValueError:
                    print("Enter a valid ID")

            case "0":
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    asyncio.run(main())