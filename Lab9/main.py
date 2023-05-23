import mysql.connector
import tkinter as tk

connection1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Spiderman_123'
)
myCursor=connection1.cursor()
myCursor.execute("CREATE DATABASE IF NOT EXISTS MarvelInformations")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Spiderman_123',
    database='MarvelInformations'
)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                  ID int(3) NOT NULL,
                  Movie varchar(80) NOT NULL,
                  DateInfo varchar(50) NOT NULL,
                  Mcu_Phase varchar(20))''')

# Task 1
with open('marvel.txt', 'r') as file:
    next(file)
    for line in file:
        line = line.strip()
        data = line.split('\t')

        movie_id = int(data[0])
        movie_title = data[1]
        release_date = data[2]
        mcu_phase = data[3]

        # Task 2
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Spiderman_123',
            database='MarvelInformations'
        )
        cursor = connection.cursor()

        # Task 3
        insert_query = """
            INSERT INTO movies (ID, Movie, DateInfo, Mcu_Phase)
            VALUES (%s, %s, %s, %s)
        """
        values = (movie_id, movie_title, release_date, mcu_phase)
        cursor.execute(insert_query, values)

        connection.commit()
        cursor.close()
        connection.close()

# Task 4
window = tk.Tk()
window.title(' Marvel Movies Database')

# Task 5
def on_dropdown_select(event):
    selected_id = dropdown_var.get()
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, f"Selected ID: {selected_id}")

label_dropdown = tk.Label(window, text='Select ID:')
label_dropdown.pack()

dropdown_var = tk.StringVar(window)
dropdown = tk.OptionMenu(window, dropdown_var, *range(1, 100), command=on_dropdown_select)
dropdown.pack()

# Task 6
def add_entry():
    entry_window = tk.Toplevel()
    entry_window.title('Add Entry')

button_add = tk.Button(window, text='Add', command=add_entry)
button_add.pack()

# Task 7
def list_all_entries():
    text_box.delete('1.0', tk.END)

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Spiderman_123',
        database='MarvelInformations'
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    for row in rows:
        entry = f"ID: {row[0]}\n"
        entry += f"Movie: {row[1]}\n"
        entry += f"Date: {row[2]}\n"
        entry += f"MCU Phase: {row[3]}\n\n"
        text_box.insert(tk.END, entry)

    cursor.close()
    connection.close()

button_list_all = tk.Button(window, text='LIST ALL', command=list_all_entries)
button_list_all.pack()

text_box = tk.Text(window)
text_box.pack()

window.mainloop()