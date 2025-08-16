# 🤖 Telegram Concise AI Assistant

This is a straightforward Telegram bot that provides brief, direct answers to user messages by leveraging AI API.

---

## ✨ Features

- **Concise AI Responses:** Fetches short, one-to-two sentence answers from an AI model.
- **Secure Configuration:** Securely loads sensitive API tokens from a `.env` file.

---

## 🚀 Getting Started

Follow these steps to set up and run the bot locally.

### Prerequisites

You will need the following API tokens:
1.  **A Telegram Bot Token:** Obtain this by talking to [@BotFather](https://telegram.me/BotFather) on Telegram.
2.  **A GitHub Token:** This token requires access to the GitHub AI Inference API endpoint.

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/saprykins/telegram_test_bot
    cd telegram_test_bot
    ```

2.  **Create and activate a virtual environment:**
    -   **On macOS/Linux:**
        ```
        virtualenv venv
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```
        py -m venv venv
        venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

### Configuration

1.  In the root directory of the project, create a file named `.env`.
2.  Add your API tokens to this file as shown below, replacing the placeholder values.

    ```
    TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
    ```

### Running the Bot

Execute the following command from your terminal:

```
python bot.py
```

## ✨ Future improvements  
Enrich default settings  
Use the bot in groups  
Bot inserts data into google sheets or database  
Voice to text  


<!--
# Sources
# Official doc from telegram:  
https://core.telegram.org/bots
https://core.telegram.org/bots/api
https://github.com/python-telegram-bot/python-telegram-bot
-->

