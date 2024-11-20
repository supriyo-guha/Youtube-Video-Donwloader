# from pytube import YouTube
#
#link = YouTube("https://www.youtube.com/watch?v=8sxzVtqoAnA")
#
#video = link.streams.get_highest_resolution()
#
#video.download("G:\Torrent Downloads")

import yt_dlp

def download_youtube_video(url, output_path="."):
    try:
        # Set download options
        ydl_opts = {
            'format': 'best',  # Download the best single file format (non-adaptive)
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded successfully to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the YouTube video
    video_url = input("Enter the YouTube video URL: ").strip()

    # Optional: specify the output directory
    output_directory = input("Enter the output directory (or press Enter for current directory): ").strip()
    if not output_directory:
        output_directory = "."

    download_youtube_video(video_url, output_directory)

