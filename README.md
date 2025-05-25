# 🛠 Python Automation Projects

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

This repository contains a collection of projects and scripts focused on **automating everyday tasks with Python**. While it was initially inspired by the book [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart, the scope has grown to include personal experiments, studies, and practical tools in Python automation.

## 🎯 Purpose

The goal of this repository is to **practice and reinforce Python programming skills** by building automation scripts that solve real-world problems. These projects involve working with files, organizing folders, generating content, and more.

## 🚀 What You'll Find Here

This repository includes:

- ✅ Projects inspired by the book
- 🧪 Independent automation tools and experiments
- ⚙️ Small utilities to automate boring tasks
- 📝 Notes and personal improvements

---

## 📁 Project Structure

```
Python-Automation-Projects/
│
├── project_quiz_generator/ # Random quiz file generator
├── project_file_organizer/ # Script to organize files by extension
├── README.md
└── ...
```
---

## 🧠 Featured Projects

### 📄 File Organizer by Extension

This project automatically organizes files in a directory by their file extensions. It moves each file into a folder named after its extension, helping keep your workspace clean and organized.

**Key Features:**
- Handles files without extensions
- Prevents overwriting by renaming duplicates
- Logs all actions to a log file
- Supports CLI arguments to specify target directory

📁 Example:

```
Before:
Downloads/
├── report.pdf
├── photo.jpg
├── script.py

After:
Downloads/
├── PDF/
│ └── report.pdf
├── JPG/
│ └── photo.jpg
├── PY/
│ └── script.py
```

#### ▶️ How to Run

```bash
# Default: organizes the Downloads folder
python organizer.py

# Or specify a folder
python organizer.py "C:\Users\yourname\Documents\MyFiles"
```
#### ⏰ **Automate Daily Execution on Windows**
You can schedule the file_organizer.py script to run automatically once a day using the Windows Task Scheduler. This keeps your folders organized without manual effort.

#### 🧭 **Step-by-Step Instructions**
1. **Open Task Scheduler** 
  - Press Win + R, type taskschd.msc, and press Enter.


  
2. **Create a New Task**
 - In the right-hand panel, click on "Create Task".
3. **General Tab** 
  - Name: File Organizer
  - Check: "Run with highest privileges"
  - Choose: "Run only when user is logged on"
4. **Triggers Tab**
  - Click "New..."
  - Begin the task: On a schedule
  - Settings: the schedule frequency that suits you (e.g., Daily, Weekly, Monthly, or Hourly)
  - Start: Choose your preferred time (e.g., 08:00 AM)
5. **Actions Tab**
  - Click "New..."
  - Action: Start a program
  - Program/script:
  ```bash
  python
  ```
  - **Add arguments (replace with your actual script path):**  :
  ```bash
  "C:\Users\YourUsername\Documents\Python\organizer\organizer.py"
  ```
6. **Conditions Tab (Optional)**
 - Uncheck "Start the task only if the computer is on AC power" if you're on a laptop.
7. **Save and Run**
- Click OK to save.
- To test it, right-click your task and select "Run".

✅ Done! Your folder will be organized automatically every day.

---

### 🧠 Generate Random Quiz Files

This project generates multiple-choice quizzes on U.S. state capitals, where each quiz is randomly ordered and has a corresponding answer key.

**Skills Practiced:**
- Working with dictionaries
- File I/O and formatting
- Loops and logic
- Randomization

---

## 🛠 Technologies

- Python 3.x
- Standard Library only (unless otherwise noted)

---

## 📌 Status

This repository is an ongoing study log and toolset. I’m continuing to build more projects to automate different kinds of tasks. Contributions, feedback, or ideas are welcome!

---

## 📬 Contact

Feel free to reach out if you have ideas or questions — or just want to geek out about Python automation!

