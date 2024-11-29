To-Do List Application Documentation
Overview
The To-Do List Application is a simple GUI-based task management tool built using Python's Tkinter library. The application allows users to add, remove, and clear tasks from a list, providing an intuitive interface for managing daily tasks.

Features
Add Task: Users can input a task and add it to the list.
Remove Selected Task: Users can select a task from the list and remove it.
Clear All Tasks: Users can clear all tasks from the list with a single button click.
Requirements
Python 3.x
Tkinter library (usually included with Python installations)
Installation
Ensure you have Python installed on your system.
Copy the provided code into a Python file, e.g., todo_list.py.
Run the script using the command:
bash

Verify

Open In Editor
Edit
Copy code
python todo_list.py
Code Explanation
Imports
python

Verify

Open In Editor
Edit
Copy code
import tkinter as tk
This line imports the Tkinter library, which is used to create the graphical user interface.

Functions
add_task()

Retrieves the text from the entry field.
If the entry is not empty, it adds the task to the listbox and clears the entry field.
python

Verify

Open In Editor
Edit
Copy code
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
remove_task()

Attempts to remove the selected task from the listbox.
If no task is selected, it handles the exception gracefully.
python

Verify

Open In Editor
Edit
Copy code
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass
clear_tasks()

Clears all tasks from the listbox.
python

Verify

Open In Editor
Edit
Copy code
def clear_tasks():
    listbox.delete(0, tk.END)
GUI Setup
Window Configuration

python

Verify

Open In Editor
Edit
Copy code
root = tk.Tk()
root.title("To-Do List Application")
root.config(bg="#227093")
Initializes the main application window with a title and background color.

Entry Field

python

Verify

Open In Editor
Edit
Copy code
entry = tk.Entry(root, width=40, font=font, bg="#74cbf2")
entry.pack(pady=10)
Creates an entry field for users to input tasks.

Buttons

Add Task Button
python

Verify

Open In Editor
Edit
Copy code
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#487d94", font=font)
add_button.pack(pady=5)
Remove Task Button
python

Verify

Open In Editor
Edit
Copy code
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, bg="#487d94", font=font)
remove_button.pack(pady=5)
Clear All Tasks Button
python

Verify

Open In Editor
Edit
Copy code
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#487d94", font=font)
clear_button.pack(pady=5)
Listbox

python

Verify

Open In Editor
Edit
Copy code
listbox = tk.Listbox(root, width=30, height=8, font=("Centaur", 14), bg="#74cbf2")
listbox.pack(pady=10)
Displays the list of tasks.

Main Loop
python

Verify

Open In Editor
Edit
Copy code
root.mainloop()
Starts the Tkinter event loop, allowing the application to run and respond to user inputs.

Customization
Colors and Fonts: You can customize the colors and fonts by modifying the bg and font parameters in the respective widgets.
Functionality: Additional features can be added, such as saving tasks to a file or loading tasks from a file.
Conclusion
This To-Do List Application serves as a basic example of how to create a GUI application using Tkinter. It can be expanded with more features and functionality as needed.




