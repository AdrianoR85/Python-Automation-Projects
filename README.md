# Python Project Portfolio

Hello! This repository serves as my central portfolio, dedicated to showcasing my Python skills through a variety of hands-on projects. Here you'll find everything from web applications and automation scripts to data analysis studies. Please browse the menu below to explore each project individually.

<p align="center">
  <img src="https://img.shields.io/badge/Web_Development-007ACC?style=for-the-badge&logo=w3c&logoColor=white" alt="Web Development"/>
  <img src="https://img.shields.io/badge/Data_Science-9B59B6?style=for-the-badge&logo=pydatadotorg&logoColor=white" alt="Data Science"/>
  <img src="https://img.shields.io/badge/Automation-F5428D?style=for-the-badge&logo=robotframework&logoColor=white" alt="Automation"/>
  <img src="https://img.shields.io/badge/Desktop_Apps-5E5C64?style=for-the-badge&logo=gnome&logoColor=white" alt="Desktop Apps"/>
  <img src="https://img.shields.io/badge/APIs_&_Microservices-6B21A8?style=for-the-badge&logo=serverless&logoColor=white" alt="APIs & Microservices"/>
  <img src="https://img.shields.io/badge/Machine_Learning-00A693?style=for-the-badge&logo=openai&logoColor=white" alt="Machine Learning"/>
</p>

## 📋 Projects Menu

Here is a list of all projects contained in this repository. Click on a name to be directed to its detailed description.

- [File Organization](#-File-Organization)
- [Project Name 2](#-project-2)
- [Project Name 3](#-project-3)

---
## 🚀 File Organization <img src="https://img.shields.io/badge/Automation-F5428D?style=for-the-badge&logo=robotframework&logoColor=white" alt="Automation"/>
### Description
This project is a Python automation script that organizes files in a specified folder (default: Downloads) into subfolders based on their extensions.
It automatically creates the necessary folders, handles duplicate filenames by adding a counter, and logs all actions in a .txt file..

### Technologies Used
<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> 
<img src="https://img.shields.io/badge/Pathlib-222222?style=for-the-badge&logo=python&logoColor=white" alt="Pathlib"/>
<img src="https://img.shields.io/badge/Shutil-404040?style=for-the-badge&logo=python&logoColor=white" alt="Shutil"/> 
<img src="https://img.shields.io/badge/Unittest-6B21A8?style=for-the-badge&logo=python&logoColor=white" alt="Unittest"/>
</p>

### Project Structure
```📂 project_root
 ├── organizer.py        # Main script
 ├── organizer_log.txt   # Log file generated automatically
 ├── test/
 │   └── test.py         # Unit tests
 ├── README.md           # Project documentation
```

### Features
- Organizes files by extension into separate folders.
- Creates missing folders automatically.
- Avoids overwriting files with the same name by renaming them.
- Generates a detailed log of all actions.
- Includes automated unit tests.

### ▶️ How to Run

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

### Example
Before
``` 
Downloads/
 ├── report.pdf
 ├── image.png
 ├── script.py
```

After
```
Downloads/
 ├── PDF/
 │   └── report.pdf
 ├── PNG/
 │   └── image.png
 ├── PY/
 │   └── script.py
```

---

### 🧠 Generate Random Quiz Files

This project generates multiple-choice quizzes on U.S. state capitals, where each quiz is randomly ordered and has a corresponding answer key.

**Skills Practiced:**
- Working with dictionaries
- File I/O and formatting
- Loops and logic
- Randomization

---

## 📬 Contact

Feel free to reach out if you have ideas or questions — or just want to geek out about Python!

