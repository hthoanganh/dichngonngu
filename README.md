# Ứng dụng Dịch thuật Đa ngôn ngữ của Hoàng Anh / Hoang Anh's language translation app
![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![PyQt5](https://img.shields.io/badge/Qt-PyQt5-green.svg) ![API](https://img.shields.io/badge/API-Google_Translate-red.svg)

A desktop translation application built with Python and the PyQt5 library. The program allows users to translate text between various languages quickly and intuitively, using the Google Translate API as the backend. The application also comes with useful features such as automatic language detection, language swapping, and translation history.

## 📸 Demo / Screenshots

**Main Translation Interface:**
![Hoang Anh's language translation app_ảnh bìa](https://github.com/user-attachments/assets/214b5872-af6c-4ed4-a63c-c82a7d7bc023)

*An animated GIF demonstrating the auto-translation feature would be very impressive here!*
![loading](https://github.com/user-attachments/assets/028af9d7-8b9f-4c5f-98a6-a3afcf2b6dce)


**Translation History Window:**
![image](https://github.com/user-attachments/assets/345e1d8c-21fc-46f6-b799-fbf9bc148878)

## ✨ Key Features

* **Multi-language Translation:** Supports translation between 10+ common languages:
    * Vietnamese, English, Japanese, Chinese, Korean, German, French, Russian, Spanish, and Arabic.
* **Auto-detect Language:** Automatically identifies the source language as the user types.
* **Near Real-time Translation:** The program automatically translates after a short pause in typing, no button press required.
* **Swap Languages:** Easily swap the source and target languages, along with their text content, with a single click.
* **Translation History:**
    * Automatically saves all translations.
    * Displays history clearly grouped by date.
    * Allows for clearing the entire history.
* **Modern UI:**
    * Displays the current date.
    * Utilizes a smooth loading animation (GIF) on startup and during time-consuming tasks for a better user experience.

## 🛠️ Tech Stack

* **Language:** Python 3
* **User Interface (GUI):** PyQt5
* **Translation Library:** `googletrans` (an unofficial library for the Google Translate API)
* **Tools:** Qt Designer, PyCharm/VS Code

## 🚀 Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/hthoanganh/dichngonngu.git]
cd dichngonngu
```

**2. Create and activate a virtual environment:**
*Recommended to avoid conflicts with other Python libraries on your system.*
```bash
# Create a virtual environment (on Windows)
python -m venv .venv

# Activate the virtual environment (on Windows)
.\.venv\Scripts\activate
```

**3. Install necessary libraries:**
*All required libraries are listed in the `requirements.txt` file.*
```bash
pip install -r requirements.txt
```

**4. Directory Structure:**
*Ensure you have a directory named `load` containing the `loading.gif` file for the animation to work.*
```
your-project-folder/
│
├── main.py
├── dichngonngu.py
├── lichsu.py
├── requirements.txt
└── load/
    └── loading.gif
```

**5. Run the application:**
```bash
python main.py
```
**6. Video


---

https://github.com/user-attachments/assets/9e9501b4-129d-401f-bae6-0d64fad211d5


Thank you for checking out this project!
