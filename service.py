from connection import connection_db


async def create_task(title):
    conn = None

    try:
        conn = await connection_db()

        await conn.execute("""
            INSERT INTO tasks (title)
            VALUES ($1)
        """, title)

        print("Task created successfully")

    except Exception as error:
        print(f"Create task error: {error}")

    finally:
        if conn is not None:
            await conn.close()


async def get_tasks():
    conn = None

    try:
        conn = await connection_db()

        tasks = await conn.fetch("""
            SELECT * FROM tasks
            ORDER BY task_id
        """)

        return tasks

    except Exception as error:
        print(f"Get tasks error: {error}")
        return []

    finally:
        if conn is not None:
            await conn.close()


async def delete_task(task_id):
    conn = None

    try:
        conn = await connection_db()

        result = await conn.execute("""
            DELETE FROM tasks
            WHERE task_id = $1
        """, task_id)

        if result == "DELETE 0":
            print("Task not found")
        else:
            print("Task deleted successfully")

    except Exception as error:
        print(f"Delete task error: {error}")

    finally:
        if conn is not None:
            await conn.close()