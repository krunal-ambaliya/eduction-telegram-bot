# EduSmart Telegram Bot 📚🤖

EduSmart is a custom-built Telegram bot that helps students quickly access their **department-specific** study resources like **textbooks**, **syllabus**, and **timetable**. The bot supports **multi-semester** navigation and provides **file or link-based** content instantly through a guided conversation.

## 🔍 Features

- Department selection (e.g., IT, Mechanical, Civil)
- Semester-wise categorization (Sem 1 to Sem 6)
- Category filtering:
  - 📘 Textbooks
  - 📄 Syllabus
  - 🕒 Timetable
- Easy navigation with options to go Back or Cancel
- Sends files using Telegram's `file_id` or public URLs

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.7+
- Telegram Bot Token from [BotFather](https://t.me/BotFather)
- `python-telegram-bot` library

### Installation

1. **Clone the Repository** (or create your own project file):
    ```bash
    git clone https://github.com/yourusername/edusmart-bot.git
    cd edusmart-bot
    ```

2. **Install Required Packages**:
    ```bash
    pip install python-telegram-bot==13.15
    ```

3. **Update Your Bot Token** in the code:
    ```python
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    ```

4. **Run the Bot**:
    ```bash
    python NewMain.py
    ```

---

## 🚀 How to Use

1. **Start the Bot**: Type `/start` in the Telegram chat.
2. **Choose Department**: Select `IT`, `Mechanical`, or `Civil`.
3. **Pick Your Semester**: For example, `sem 1`.
4. **Choose a Category**:
   - `Timetable`: Sends the timetable (PDF or link).
   - `Textbook`: Choose subject → receive textbook.
   - `Syllabus`: Choose subject → receive syllabus.
5. **Go Back** or `/cancel` anytime to restart.

---
## 📬 Contact
For more Telegram bot projects or help with bot development, feel free to contact me:

**Telegram**: [@krues](https://t.me/KRUES)
