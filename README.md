# 📤 telegram-media-forwarder 🚀

Welcome to **telegram-media-forwarder**! 🎉 This Telegram bot script uses Telethon to manage and forward media and text messages across channels. Perfect for automating message forwarding, promoting channels, and keeping your storage clean! 🌟

![Telegram Media Forwarder](https://erfan4lx.com/wp-content/uploads/2022/09/Telegram-Channel-Posts-Forwarder-2.png) <!-- Example image -->

## 🛠 Features

- **📩 Forwarding Messages:** Automatically forwards text and media messages from specified source channels to a target channel.
  ![Forwarding Messages](https://erfan4lx.com/wp-content/uploads/2022/09/Telegram-Channel-Posts-Forwarder-2.png) <!-- Use this or a relevant image -->
- **🔔 Periodic Promotions:** Sends periodic messages to invite users to join the target channel.
  ![Periodic Promotions](https://example.com/periodic-promotions.png) <!-- Replace with your own image -->
- **🗑 File Management:** Downloads media files, tracks them, and deletes them after 30 minutes to save storage space.
  ![File Management](https://example.com/file-management.png) <!-- Replace with your own image -->

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/telegram-media-forwarder.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd telegram-media-forwarder
    ```

3. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install the required dependencies:**

    ```bash
    pip install telethon
    ```

6. **Update the script** with your API credentials and channel details in `msg.py`.

7. **Run the script:**

    ```bash
    python msg.py
    ```

## 🌟 Usage

- Make sure your `api_id`, `api_hash`, and `phone_number` are set correctly. 🔐
- Modify `source_channels` and `target_channel` with the appropriate values in the script. 📡
- The bot will handle forwarding messages, sending join promotions, and managing files as specified. 📤

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📜

## 💡 Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Contributions are always welcome! 🤝

## 📞 Contact

For any issues or inquiries, please open an issue on the [GitHub repository](https://github.com/yourusername/telegram-media-forwarder/issues). 🚀

---

Happy forwarding! 🎉✨
