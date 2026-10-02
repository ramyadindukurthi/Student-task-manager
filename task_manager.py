import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()


# Add a new task
def add_task():
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    cursor.execute(
        "INSERT INTO tasks (task, status) VALUES (?, ?)",
        (task, "Pending")
    )

    conn.commit()

    print("Task added successfully!")


# View all tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== Your Tasks =====")

    for task in tasks:
        print(f"{task[0]}. {task[1]} - {task[2]}")


# Mark a task as completed
def complete_task():
    view_tasks()

    task_id = input("\nEnter task ID to mark as completed: ")

    cursor.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("Task not found.")
    else:
        print("Task marked as completed!")


# Delete a task
def delete_task():
    view_tasks()

    task_id = input("\nEnter task ID to delete: ")

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("Task not found.")
    else:
        print("Task deleted successfully!")


# Main menu
while True:

    print("\n==============================")
    print("     STUDENT TASK MANAGER")
    print("==============================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Student Task Manager!")

        break

    else:
        print("Invalid choice. Please try again.")


# Close database connection
conn.close()
