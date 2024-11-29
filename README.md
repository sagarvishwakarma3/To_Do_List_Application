## **Documentation: To-Do List Application**

### **Overview**
This project implements a **To-Do List Application** using Python's `tkinter` library. The application provides a simple, user-friendly graphical interface for managing tasks. Users can add, remove, and clear tasks through buttons and input fields.

---

### **Objective**
To build a lightweight and visually appealing task management tool that introduces basic GUI concepts such as buttons, entry fields, and listboxes.

---

### **Key Features**
1. **Add Task**: Users can enter a task into a text input field and add it to the list.
2. **Remove Selected Task**: Deletes a specific task selected from the list.
3. **Clear All Tasks**: Removes all tasks from the list at once.

---

### **Technologies Used**
- **Programming Language**: Python
- **GUI Library**: `tkinter`

---

### **Application Design**

#### **1. GUI Layout**
- **Main Window**:
  - Title: `"To-Do List Application"`.
  - Background Color: `#227093` (calming blue tone).
- **Font Style**: `"Centaur", size 14` for consistency across widgets.
- **Color Scheme**:
  - Entry Field Background: `#74cbf2` (light blue).
  - Button Background: `#487d94` (blue-gray).

#### **2. Widgets**
- **Entry Field**: 
  - Accepts user input for tasks.
  - Positioned at the top of the window.
- **Buttons**:
  - **Add Task**: Adds tasks from the entry field to the listbox.
  - **Remove Selected Task**: Deletes the highlighted task in the listbox.
  - **Clear All Tasks**: Empties the entire listbox.
- **Listbox**:
  - Displays tasks added by the user.
  - Positioned below the buttons.

---

### **Code Explanation**

#### **1. Importing tkinter Library**
```python
import tkinter as tk
```
The `tkinter` library is imported to create the graphical user interface.

#### **2. Define Functions**
- **Add Task**:
  - Reads text from the entry field.
  - Adds the task to the listbox.
  - Clears the entry field after adding.
  ```python
  def add_task():
      task = entry.get()
      if task:
          listbox.insert(tk.END, task)
          entry.delete(0, tk.END)
  ```

- **Remove Selected Task**:
  - Deletes the task selected in the listbox.
  - Includes error handling to prevent crashes when no task is selected.
  ```python
  def remove_task():
      try:
          selected_task_index = listbox.curselection()[0]
          listbox.delete(selected_task_index)
      except IndexError:
          pass
  ```

- **Clear All Tasks**:
  - Removes all tasks from the listbox.
  ```python
  def clear_tasks():
      listbox.delete(0, tk.END)
  ```

#### **3. Create the Main Application Window**
- Define the root window with:
  - **Title**: `"To-Do List Application"`.
  - **Background Color**: `#227093`.
  ```python
  root = tk.Tk()
  root.title("To-Do List Application")
  root.config(bg="#227093")
  ```

#### **4. Add Widgets**
- **Entry Widget**: 
  - Accepts task input.
  - Configured with a width of 40 and background color `#74cbf2`.
  ```python
  entry = tk.Entry(root, width=40, font=font, bg="#74cbf2")
  entry.pack(pady=10)
  ```

- **Buttons**:
  - Positioned with vertical spacing (`pady=5`).
  - Associated with the corresponding functions using `command`.
  ```python
  add_button = tk.Button(root, text="Add Task", command=add_task, bg="#487d94", font=font)
  remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, bg="#487d94", font=font)
  clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#487d94", font=font)
  add_button.pack(pady=5)
  remove_button.pack(pady=5)
  clear_button.pack(pady=5)
  ```

- **Listbox**:
  - Displays the list of tasks.
  - Configured with width, height, and consistent font styling.
  ```python
  listbox = tk.Listbox(root, width=30, height=8, font=("Centaur", 14), bg="#74cbf2")
  listbox.pack(pady=10)
  ```

#### **5. Run the Application**
The `mainloop()` method starts the event loop for the application, making the GUI interactive.
```python
root.mainloop()
```

---

### **Complete Code**
```python
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
root.config(bg="#227093")

font = ("Centaur", 14)

entry = tk.Entry(root, width=40, font=font, bg="#74cbf2")
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#487d94", font=font)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, bg="#487d94", font=font)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#487d94", font=font)
clear_button.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=8, font=("Centaur", 14), bg="#74cbf2")
listbox.pack(pady=10)

root.mainloop()
```

---

### **How to Use**
1. **Run the Script**: Execute the Python file to launch the application.
2. **Add Tasks**:
   - Enter text in the input field.
   - Click "Add Task" to add it to the list.
3. **Remove Tasks**:
   - Select a task in the listbox.
   - Click "Remove Selected Task" to delete it.
4. **Clear All Tasks**:
   - Click "Clear All Tasks" to empty the list.

---

### **Error Handling**
- Prevents crashes when:
  - No task is selected for removal (handled using `try-except` block).
  - Attempting to add an empty task (ignores blank inputs).

---

### **Conclusion**
The **To-Do List Application** is a practical project for beginners exploring GUI programming in Python. It demonstrates the use of widgets, event-driven programming, and simple error handling, making it a foundational project for further exploration.
