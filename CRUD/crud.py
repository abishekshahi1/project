import mysql.connector

try:
    root_conn = mysql.connector.connect(
        host="localhost",
        user="root",     
        password="root"   
    )
    root_cursor = root_conn.cursor()
    root_cursor.execute("CREATE DATABASE crud_demo") 
    print("Database created successfully.")
except Exception as e:
    print("Error creating database (maybe already exists):", e)

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="crud_app"
    )
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    ''')
    print("Table created successfully.")

except Exception as e:
    print("Error connecting or creating table:", e)

# CREATE
def create_user():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        print("User added.")
    except Exception as e:
        print("Error adding user:", e)

# READ
def read_users():
    try:
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print("Error reading users:", e)

# UPDATE
def update_user():
    try:
        uid = int(input("Enter user ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, uid))
        conn.commit()
        print("User updated.")
    except Exception as e:
        print("Error updating user:", e)

# DELETE
def delete_user():
    try:
        uid = int(input("Enter user ID to delete: "))
        cursor.execute("DELETE FROM users WHERE id=%s", (uid,))
        conn.commit()
        print("User deleted.")
    except Exception as e:
        print("Error deleting user:", e)

def menu():
    while True:
        print("\nCRUD MENU")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

menu()
cursor.close()
conn.close()
root_cursor.close()
root_conn.close()