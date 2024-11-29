# **To-Do List Application**

## **Overview**
The **To-Do List Application** is a simple GUI-based project developed using Python's `tkinter` library. This application allows users to manage their daily tasks efficiently by adding, removing, and clearing tasks from a list.

---

## **Features**
1. **Add Tasks**:
   - Enter a task in the input field and add it to the list by clicking the "Add Task" button.
2. **Remove Selected Task**:
   - Select a task from the list and click "Remove Selected Task" to delete it.
3. **Clear All Tasks**:
   - Quickly clear the entire task list with a single button click.
4. **Intuitive User Interface**:
   - Simple, user-friendly design with a responsive layout.

---

## **How It Works**

### **1. Adding a Task**
- Enter a task in the input field.
- Click the "Add Task" button to append the task to the task list.

### **2. Removing a Task**
- Select a task from the list by clicking on it.
- Click the "Remove Selected Task" button to delete the selected task.

### **3. Clearing All Tasks**
- Click the "Clear All Tasks" button to remove all tasks from the list.

---

## **Prerequisites**
- **Python Version**: Requires Python 3.6 or higher.
- No additional libraries are needed as `tkinter` is part of Python's standard library.

---

## **How to Run the Application**

1. **Save the Script**:
   Save the code as `todo_list.py` or a similar name.

2. **Run the Script**:
   Open a terminal or command prompt and execute:
   ```bash
   python todo_list.py
   ```

3. **Use the Application**:
   - Add, remove, and clear tasks as needed.

---

## **Code Explanation**

### **1. Functions**
- **`add_task()`**:
  - Retrieves the text from the input field and adds it to the listbox.
  - Clears the input field after adding the task.
- **`remove_task()`**:
  - Deletes the currently selected task from the listbox.
  - Handles cases where no task is selected.
- **`clear_tasks()`**:
  - Clears all tasks from the listbox.

### **2. GUI Components**
- **Main Window**:
  - Created using `tk.Tk()`, with the title "To-Do List Application".
  - Background color set to a calming blue (`#227093`).
- **Input Field**:
  - `tk.Entry` widget to enter tasks.
  - Styled with a modern font (`Centaur`) and background color (`#74cbf2`).
- **Buttons**:
  - Three buttons for adding, removing, and clearing tasks.
  - Styled with distinct colors and a consistent font.
- **Task List**:
  - `tk.Listbox` widget to display tasks in a list format.
  - Styled to match the application's design.

---

## **Code**
```python
import tkinter as tk

# Function to add a task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

# Function to clear all tasks from the list
def clear_tasks():
    listbox.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("To-Do List Application")
root.config(bg="#227093")

# Define font
font = ("Centaur", 14)

# Input field
entry = tk.Entry(root, width=40, font=font, bg="#74cbf2")
entry.pack(pady=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#487d94", font=font)
add_button.pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=30, height=8, font=("Centaur", 14), bg="#74cbf2")
listbox.pack(pady=10)

# Remove Task button
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, bg="#487d94", font=font)
remove_button.pack(pady=5)

# Clear Tasks button
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#487d94", font=font)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
```

---

## **Example Workflow**
1. Launch the application.
2. Add tasks:
   - Input: `Buy groceries` → Click "Add Task".
   - Input: `Complete homework` → Click "Add Task".
3. Remove a task:
   - Select `Complete homework` → Click "Remove Selected Task".
4. Clear all tasks:
   - Click "Clear All Tasks".

---

## **Benefits**
- Simplifies task management.
- Provides a hands-on introduction to GUI development with Python.
- Easy to modify and extend with additional features.

---

## **Future Enhancements**
1. Add a **task editing feature** to update existing tasks.
2. Include **task categorization** for better organization.
3. Integrate **task saving and loading** functionality to maintain the task list between sessions.
4. Enhance the UI with advanced styling or frameworks like `ttk`.

---

## **Conclusion**
This **To-Do List Application** is a straightforward and efficient tool for managing tasks. It serves as an excellent beginner project to learn about GUI programming with `tkinter` and can be easily customized for advanced use cases.
