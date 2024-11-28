import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Application")

# Set background color of the window to #227093
root.config(bg="#227093")

# Define the font as Centaur and set size for the entry, buttons, and listbox
font = ("Centaur", 14)

# Set the size of the entry field and its font
entry = tk.Entry(root, width=40, font=font, bg="#74cbf2")
entry.pack(pady=10)

# Set the font and size for the buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#487d94", font=font)
add_button.pack(pady=5)

# Set the font, size, and background color for the listbox
listbox = tk.Listbox(root, width=30, height=8, font=("Centaur", 14), bg="#74cbf2")
listbox.pack(pady=10)

# Set the font and size for the remove button
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, bg="#487d94", font=font)
remove_button.pack(pady=5)

# Set the font and size for the clear button
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#487d94", font=font)
clear_button.pack(pady=5)

root.mainloop()
