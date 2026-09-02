# Download internet videos on your own server

Reclip, developed by Averygan, is a lightweight, self-hostable tool for downloading videos from almost any website. It allows you to save media files to your local device through a simple web interface.

- ★ 7,951
- HTML
- GitHub Trending · 2026-09-02

## What you get
- Downloads video and audio files from over 1000 sites such as YouTube and Instagram.
- Saves downloaded files in MP4 video or MP3 audio format.
- Offers a simple and fast interface that runs through a web browser.

## Installation
**Standard installation**

```
brew install yt-dlp ffmpeg    # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Installation with Docker**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```


## Running it
**Access to interface**

```
http://localhost:8899
```


## If you don't write code
I want to download video links from the internet to my local device in MP4 or MP3 format using the Reclip tool. To start the download process, I need to paste the links into the input box, select the format, click the Fetch button to load the video information, and then use the Download button. During this process, I can perform bulk downloads and adjust the video resolution according to my preferences.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/reclip/
