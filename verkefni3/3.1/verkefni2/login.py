import sqlite3

def login():
    while True:
        username = input("Enter name")
        password = input("Password")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            print(results)
            for i in results:
                print("Welcome "+i[2])
            break

        else:
            print("Incorrect")

def new_user():
    while True:
        username = input("Enter new name")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(find_user, [(username)])

        if cursor.fetchall():
            print("User exists")

        else:
            break

    password = input("New Password")
    firstname = input("First name")
    surname = input("Surname")
    new_user = "INSERT INTO user(username,password,firstname,surname) VALUES(?,?,?,?)"
    cursor.execute(new_user, [(username),(password),(firstname),(surname)])
    db.commit()

new_user()
