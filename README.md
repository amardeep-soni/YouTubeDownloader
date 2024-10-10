# HD YouTube Video and Playlist Downloader

This Python script allows you to download individual videos or entire playlists from YouTube using the `yt_dlp` library. The downloaded videos are saved in the highest available quality (best video and audio) and merged into `mp4` format using `FFmpeg`.

## Features

- Download individual YouTube videos in the best available quality.
- Download entire YouTube playlists.
- Output files saved in a user-defined folder with descriptive names.
- Merges best video and best audio into a single `mp4` file using `FFmpeg`.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- `yt_dlp` library (a fork of `youtube-dl`)
- `FFmpeg` (required for merging video and audio)
- change the drive name and folder name where you want to save the downloaded video

### Install yt-dlp

You can install `yt_dlp` using pip:

```bash
pip install yt-dlp
```

# FFmpeg Installation on Windows

FFmpeg is a powerful multimedia framework that can decode, encode, transcode, mux, demux, stream, filter, and play almost anything that humans and machines have created. This document outlines the steps to install FFmpeg on a Windows system.

## Installation Steps

For Installation Guid you can reffer the [Geeks website](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)

1. **Download FFmpeg:**

   - From Official Website

     - Go to the [FFmpeg official website](https://ffmpeg.org/download.html).
     - Click on the "Windows" logo.
     - Choose a build from the available options. It's recommended to select a build from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
     - Download the latest version (usually a zip file).

   - Direct download link of 7.1 version
     - Or Simply click on this link to download the [FFmpeg 7.1 version](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

2. **Extract the Files:**

   - Locate the downloaded zip file and extract it.
   - You can use built-in Windows extraction or tools like WinRAR or 7-Zip.
   - After extraction, you will have a folder named something like `ffmpeg-2023-10-09-git-xxxxxx-windows-amd64` or other.
   - Rename the folder to ffmpeg
   - Move that folder to **`C:`** drive

3. **Add FFmpeg to the System Path:**

   - Now, run cmd as an administrator and set the environment path variable for FFmpeg by running the following command:

     ```
     setx /m PATH "C:\ffmpeg\bin;%PATH%"
     ```

4. **Verify the Installation:**
   - Restart your computer and verify the installation by running:
   ```
   ffmpeg -version
   ```

# Credits

This project utilizes the [yt-dlp](https://github.com/yt-dlp/yt-dlp) package, an open-source YouTube downloader and video downloader tool. 

**yt-dlp** is a powerful fork of `youtube-dl` and comes with several additional features and improvements. All credit for the video downloading functionality in this script goes to the `yt-dlp` development team. You can learn more about the package or contribute to its development by visiting the [yt-dlp GitHub repository](https://github.com/yt-dlp/yt-dlp).
