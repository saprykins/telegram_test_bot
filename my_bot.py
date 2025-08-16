# This bot script requires the 'python-telegram-bot' and 'python-dotenv' libraries.
# To install them, open your terminal or command prompt and run:
# pip install python-telegram-bot python-dotenv

# First, import the necessary modules. We'll use os to get environment variables
# and dotenv to load them from the .env file.
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ApplicationBuilder

# This tells the script to look for a .env file in the current directory and
# load the variables it finds there into the environment.
load_dotenv()

# We will now securely get the token from the environment.
# It will either be set by your system or loaded from the .env file.
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# This is the function that will be executed when the '/start' command is used.
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a greeting message to the user."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="hey bro"
    )

# This is the function for our custom command, which we'll call '/think'.
async def think_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message indicating the bot is thinking."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="let me think"
    )

# The main function to set up and run the bot.
def main():
    """Starts the bot using the polling method to listen for updates."""
    # Check if the token was successfully loaded.
    if not BOT_TOKEN:
        print("Error: Bot token not found. Please create a .env file or set the TELEGRAM_BOT_TOKEN environment variable.")
        return

    # Create the application builder with our bot token.
    app_builder = ApplicationBuilder().token(BOT_TOKEN)
    
    # Build the application instance.
    application = app_builder.build()

    # Create a handler for the '/start' command and link it to our start_command function.
    start_handler = CommandHandler('start', start_command)
    
    # Create a handler for the '/think' command and link it to our think_command function.
    think_handler = CommandHandler('think', think_command)

    # Add both handlers to the application.
    application.add_handler(start_handler)
    application.add_handler(think_handler)

    # Start the bot.
    print("Bot is running...")
    application.run_polling()

# This makes sure our main function is called when the script is run.
if __name__ == '__main__':
    main()