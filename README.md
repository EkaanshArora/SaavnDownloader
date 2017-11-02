# SaavnDownloader
- Downloads songs from YouTube in an MP3 format by using Saavn's stared music.
- Automatically fixes song's meta-tags
- Works straight out of the box and does not require to generate or mess with your API keys.

## Base
Based on Ritiek's [Spotify-Downloader](https://github.com/ritiek/spotify-downloader).

## Installation & Usage
- **This tool supports only Python 3**

### Windows

Assuming you have Python 3 ([preferably v3.6 or above to stay away from Unicode errors](https://stackoverflow.com/questions/30539882/whats-the-deal-with-python-3-4-unicode-different-languages-and-windows)) already installed and in PATH.

- Download and extract the zip file from master branch.

- Download FFmpeg for Windows from [here](http://ffmpeg.zeranoe.com/builds/). Copy `ffmpeg.exe` from `ffmpeg-xxx-winxx-static\bin\ffmpeg.exe` to PATH (usually C:\Windows\System32\) or just place it in the root directory extracted from the above step.
-Download [Geckodriver]( https://github.com/mozilla/geckodriver/releases/latest). Put this in the same directory as the unzipped package.
-[Mozlla Firefox]( https://www.mozilla.org/en-US/firefox/new/).
- Open `cmd` and type `pip install -U -r requirements.txt` to install dependencies.

## Instructions for Downloading Songs

-Open file scraper.py, in a text editor, modify the email and password field to match your Saavn credentials, save and run in cmd using python scraper.py
-Don't touch your mouse or keyboard till the starred songs pages appears in the opened firefox window, the window may seem unresponsive, after the songs are listed you can check progress in the opened cmd window.

## Disclaimer

Downloading copyright songs may be illegal in your country. This tool is for educational purposes only. Please support the artists by buying their music.

## License

```The MIT License```
