from telethon import TelegramClient, events
import asyncio
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your API credentials
api_id = int(os.getenv('API_ID'))  # Your API ID
api_hash = os.getenv('API_HASH')  # Your API Hash
phone_number = os.getenv('PHONE_NUMBER')  # Your phone number with country code

# Target channel username or ID (where you want to send messages)
target_channel = os.getenv('TARGET_CHANNEL')  # Replace with your target channel's username or ID

# List of source channels (where messages are coming from)
source_channels = list(map(int, os.getenv('SOURCE_CHANNELS').split(',')))

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Dictionary to keep track of downloaded files and their download times
downloaded_files = {}

# Define the event handler for new messages
@client.on(events.NewMessage(chats=source_channels))
async def handle_new_message(event):
    try:
        # Extract message content
        message_text = event.message.text or ''
        media = event.message.media

        if media:
            # Download and send media message
            file = await client.download_media(media)
            await client.send_file(target_channel, file, caption=message_text)

            # Track the downloaded file with current time
            downloaded_files[file] = time.time()
            print(f"Message sent from {event.chat_id} to {target_channel}")

        else:
            # Send text message
            await client.send_message(target_channel, message_text)
            print(f"Message sent from {event.chat_id} to {target_channel}")

    except Exception as e:
        print(f"Error: {e}")

async def send_channel_join_message():
    while True:
        try:
            # Send a message to join the channel
            join_message = (
                "🚀 Hey there! 🌟\n\n"
                "Join our amazing channel for exclusive content and updates! 🎉📢\n\n"
                "👉 Click here to join us: [Join our Channel](https://t.me/codeTech01)\n\n"
                "Don't miss out on the fun! 😎👋\n\n"
                "See you in the channel! 🎊✨"
            )
            await client.send_message(target_channel, join_message, parse_mode='html')
            print("Join message sent to the target channel.")
        except Exception as e:
            print(f"Error sending join message: {e}")
        await asyncio.sleep(300)  # Wait for 5 minutes

async def delete_old_files():
    while True:
        current_time = time.time()
        for file_path, download_time in list(downloaded_files.items()):
            if current_time - download_time > 1800:  # 30 minutes
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
                finally:
                    del downloaded_files[file_path]
        await asyncio.sleep(60)  # Check every minute

async def main():
    # Start the client and authenticate your Telegram account
    await client.start(phone=phone_number)
    print("Listening for new messages in source channels...")

    # Run periodic tasks in the background
    client.loop.create_task(send_channel_join_message())
    client.loop.create_task(delete_old_files())

    # Run the client until disconnected
    await client.run_until_disconnected()

# Run the script
client.loop.run_until_complete(main())
