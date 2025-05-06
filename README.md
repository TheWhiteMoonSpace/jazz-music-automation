# 🎷 Jazz Music Video Automation Bot

This project automates the creation and upload of relaxing jazz music videos to YouTube. It combines audio clips, overlays a thumbnail, syncs video length, and uploads it — all in one go.

## 📁 Project Structure

```
jazz_bot/
├── audio_clips/           # Input MP3 audio clips
├── video_clips/           # Input MP4/MOV video backgrounds
├── scripts/
│   └── main.py            # Main automation script
├── client_secrets.json    # Google API credentials (not tracked by Git)
├── final_video.mp4        # Output video (auto-generated)
├── output_audio.mp3       # Combined audio (auto-generated)
├── thumbnail.jpg          # Auto-generated thumbnail
├── venv/                  # Virtual environment (not tracked by Git)
└── README.md              # You're reading this!
```

## ⚙️ Requirements

* Python 3.10 or newer
* `ffmpeg` (added to PATH)
* Google API credentials for YouTube Data API v3

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/jazz-music-automation.git
cd jazz-music-automation
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install moviepy pydub pillow google-auth google-auth-oauthlib google-api-python-client
```

### 4. Install `ffmpeg`

Download from [FFmpeg.org](https://ffmpeg.org/download.html) and extract.

Add the `/bin` folder to your system's environment PATH.

Example:

```python
# Inside main.py
os.environ["PATH"] += os.pathsep + r"C:\\ffmpeg\\bin"
```

## 📆 Usage

### 1. Place Your Input Files

* Put your `.mp3` clips in the `audio_clips/` folder.
* Put your `.mp4` or `.mov` background videos in the `video_clips/` folder.

### 2. Run the Script

```bash
python scripts/main.py
```

* It will combine audio, select a random video, trim it to match audio length, generate a thumbnail, and upload the final video to YouTube.

### 3. Authenticate

On first run, you'll be asked to authenticate via a browser popup (OAuth2).

## 🔐 Authentication

* Get `client_secrets.json` from your Google Cloud Console (OAuth 2.0 Client ID).
* Place it in the root of the project directory.

## 📆 Output

* `final_video.mp4` — The complete, uploaded video
* `output_audio.mp3` — Combined audio clip
* `thumbnail.jpg` — Thumbnail used for the video

## 🚫 .gitignore

Make sure your `.gitignore` includes:

```gitignore
venv/
*.mp4
*.mp3
*.jpg
client_secrets.json
__pycache__/
```

## 🛡️ License

MIT License

---

Created with ❤️ for lo-fi jazz automation.
