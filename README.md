# 📥 **MediaMagic Downloader** 🚀

Welcome to **MediaMagic Downloader**! 🎉 This powerful command-line tool allows you to effortlessly download videos, audio, and thumbnails from platforms like **YouTube**, **TikTok**, **Instagram**, **Spotify**, **Terabox**, and more! Whether you want to grab videos in HD, download audio-only tracks, or simply fetch a thumbnail, **MediaMagic** has got you covered. 🌟

## 🛠 Features

- **📥 Multi-Platform Support:** Download videos, audio, and thumbnails from platforms like YouTube, TikTok, Instagram, Terabox, and Spotify.  
- **🎬 Video & Audio Downloading:** Fetch videos in multiple resolutions (e.g., 720p, 1080p) or download audio in your preferred format (MP3, AAC, etc.).  
- **🔍 Fetch Media Info:** View details such as video title, duration, and quality before downloading.  
- **💾 File Management:** Download, track, and organize your media with ease. Specify output directories and avoid storage clutter.

## 🚀 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/MediaMagic-Downloader.git

```

### 2. Navigate to the project directory:

```bash
cd MediaMagic-Downloader
```

### 3. Set up a virtual environment:

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment:
#### Windows:

```bash
venv\Scripts\activate
```

#### macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install essential libraries such as:

- `yt-dlp`: A powerful video downloader.
- `ffmpeg`: A multimedia framework for video/audio processing.
- `requests`: For handling HTTP requests.
- `termcolor`: For adding color to the terminal output.

### 6. Install FFmpeg (if not already installed)
#### Windows: 
Download FFmpeg from [FFmpeg.org](https://ffmpeg.org) and add it to your PATH.

#### Linux:
Install using your package manager:

```bash
sudo apt install ffmpeg
```

### 7. Run the script:

```bash
python mediamagic
```

## 🌟 Usage
Once the tool is installed, you can use the following commands to start downloading media:

### Command Structure

```bash
python mediamagic [OPTIONS]
```

### Examples

1. **Download Media**  
To download media (video, audio, thumbnail) from a URL:

```bash
python mediamagic -u https://example.com -d -o /path/to/save
```

- `-u`: URL of the media to download.
- `-d`: Start the download process.
- `-o`: Specify the output directory.

2. **Fetch Media Information**  
To get media details without downloading:

```bash
python mediamagic -u https://example.com --info
```

- `--info`: Displays media information without initiating the download.

3. **Show Supported Platforms**  
To list all supported platforms (YouTube, TikTok, etc.):

```bash
python mediamagic --platforms
```

4. **Show Current Version**  
To display the current version of MediaMagic Downloader:

```bash
python mediamagic --version
```

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details. 📜
