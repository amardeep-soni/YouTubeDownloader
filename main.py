import os
import yt_dlp

def download_video(video_url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # Prioritize best video and audio separately
        'merge_output_format': 'mp4',  # Ensure the output is in mp4 format
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Download completed!")
    except Exception as e:
        print(f'Error downloading video: {e}')

def download_playlist(playlist_url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(playlist)s', '%(playlist_index)02d - %(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # Same as above
        'merge_output_format': 'mp4',
        'noplaylist': False,  # Ensure we are downloading the whole playlist
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            print("Playlist download completed!")
    except Exception as e:
        print(f'Error downloading playlist: {e}')

def main():
    choice = input("Enter '1' to download a single video or '2' to download a playlist: ")
    output_path = 'F:/ytVideos/'
    if choice == '1':
        video_url = input("Enter the video URL: ")
        download_video(video_url, output_path)
    elif choice == '2':
        playlist_url = input("Enter the playlist URL: ")
        download_playlist(playlist_url, output_path)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
