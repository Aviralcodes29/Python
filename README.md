# ✅ Python Study Task Manager (CLI)

A simple command-line app written in Python to manage your study tasks.  
You can add tasks, view them, mark them as done, and everything is saved in a JSON file.

---

## 🎯 Features

- Add new study tasks with a short description
- View all tasks with their status:
  - ⏳ = pending
  - ✅ = done
- Mark any task as completed by its number
- Tasks are stored in `tasks.json` so they stay even after you close the program

---

## 🧰 Tech stack

- Python 3
- JSON file for storage (no database)
- Runs in terminal / command prompt

---

## 📂 Project structure

```text
PYTHON/
│── todo.py        # main Python script (study task manager)
│── tasks.json     # stores tasks as JSON (auto-created/updated)
└── README.md      # this file
```

---

## 🚀 How to run

1. Make sure Python 3 is installed and available in PATH:

```bash
python --version
```

2. Go to the project folder in terminal:

```bash
cd PATH/TO/PYTHON
```

3. Run the app:

```bash
python todo.py
```

4. Use the menu:

- `1` → View tasks  
- `2` → Add task  
- `3` → Mark task as done  
- `4` → Exit  

---

## 🧠 Example usage

```text
=== Python Study Task Manager ===
1. View tasks
2. Add task
3. Mark task as done
4. Exit

Choose an option (1-4): 2

Enter task description: Study Python 1 hour
Task added!

Choose an option (1-4): 1

Your tasks:
1. ⏳ Study Python 1 hour

Choose an option (1-4): 3

Your tasks:
1. ⏳ Study Python 1 hour

Enter task number to mark as done: 1
Task marked as done!
```

---

## 🔮 Future improvements

- Add due date for each task
- Add priority (Low / Medium / High)
- Filter tasks (only pending / only done)
- Colorful terminal output

---

> Built by **Aviral (Aviralcodes29)** as a beginner Python project.