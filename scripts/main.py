import sys
print(sys.executable)
print(sys.path)
import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
from PIL import Image, ImageDraw, ImageFont
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


# Add ffmpeg to PATH (if not in system path)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-master-latest-win64-gpl-shared\bin"  # Adjust if your ffmpeg path is different

# Define folder paths and output filenames
AUDIO_FOLDER = r"C:\Users\Mohsi\OneDrive\Documents\jazz_bot\audio_clips"
VIDEO_CLIPS_FOLDER = r"C:\Users\Mohsi\OneDrive\Documents\jazz_bot\Video_clips"
COMBINED_AUDIO = "output_audio.mp3"
THUMBNAIL_IMAGE = "thumbnail.jpg"
OUTPUT_VIDEO = "final_video.mp4"

# Define Google API scopes for YouTube upload
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Combine all audio clips into a single file
def combine_audio_clips():
    combined = AudioSegment.empty()
    for file in os.listdir(AUDIO_FOLDER):
        if file.endswith(".mp3"):
            combined += AudioSegment.from_mp3(os.path.join(AUDIO_FOLDER, file))
    combined.export(COMBINED_AUDIO, format="mp3")
    print("✅ Combined audio saved.")

# Create a simple thumbnail image with text
def create_thumbnail(text="Jazz Vibes 🎷"):
    width, height = 1280, 720
    image = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((width - w) / 2, (height - h) / 2), text, fill="white", font=font)
    image.save(THUMBNAIL_IMAGE)
    print("✅ Thumbnail created.")

# Create a video by combining a randomly chosen video clip with the audio
def create_video_with_clip():
    audio = AudioFileClip(COMBINED_AUDIO)
    video_files = [f for f in os.listdir(VIDEO_CLIPS_FOLDER) if f.endswith((".mp4", ".mov"))]
    
    if not video_files:
        raise FileNotFoundError("No video clips found in video_clips folder.")
    
    # Choose a random video clip
    selected_video = os.path.join(VIDEO_CLIPS_FOLDER, random.choice(video_files))

    # Create a VideoFileClip object and match the duration with the audio
    video = VideoFileClip(selected_video).subclip(0, audio.duration)

    # Set the audio to the video and write the final output
    final = video.set_audio(audio)
    final.write_videofile(OUTPUT_VIDEO, codec="libx264", audio_codec="aac")
    print("✅ Video created.")

# Authenticate with Google API to upload video to YouTube
def authenticate_youtube():
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
    creds = flow.run_local_server(port=8080)
    return creds

# Upload the created video to YouTube
def upload_video_to_youtube(video_path, title="Jazz Music Vibes", description="Relaxing jazz music to study, work, or chill. 🎷"):
    creds = authenticate_youtube()
    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["jazz", "lofi", "study music", "relaxing"],
            "categoryId": "10"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)
    response = request.execute()
    print(f"✅ Video uploaded: https://youtube.com/watch?v={response['id']}")

# Main function to combine audio, create thumbnail, generate video, and upload to YouTube
def main():
    combine_audio_clips()
    create_thumbnail("Jazz Vibes 🎷")
    create_video_with_clip()
    upload_video_to_youtube(OUTPUT_VIDEO)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
