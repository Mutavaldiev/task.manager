import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()


async def connection_db():
    return await asyncpg.connect(
        port=5432,
        host="localhost",
        user="postgres",
        database="task2_db",
        password=os.getenv("PASSWORD_DB")
    )


async def create_table():
    conn = None

    try:
        conn = await connection_db()

        await conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)

        print("Table created successfully")

    except Exception as error:
        print(f"Create table error: {error}")

    finally:
        if conn is not None:
            await conn.close()