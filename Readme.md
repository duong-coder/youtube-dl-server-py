# Installation

- Create an environment

```
Mac: python3 -m venv .venv

Win: py -3 -m venv .venv
```

- Activate the environment

```
Mac:  . .venv/bin/activate
Win: .venv\Scripts\activate
```

- Install Flask
```
pip install Flask
```

# Run the project
```
flask app server/myserver run

 * Serving Flask app 'server/myserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

# Test API
- Hello world page: ```http://127.0.0.1:5000```
- Download video from youtube url: 
```
http://127.0.0.1:5000/video/download?videoUrl=https://www.youtube.com/watch?v=VBKNoLcj8jA

videoUrlhttps://www.youtube.com/watch?v=VBKNoLcj8jA
[youtube] VBKNoLcj8jA: Downloading webpage
[download] Destination: 10 Second Countdown _ After Effects-VBKNoLcj8jA.mp4
[download] 100% of 465.04KiB in 01:07
Done downloading, now converting ...
oldFilename 10 Second Countdown _ After Effects-VBKNoLcj8jA.mp4
newFilename video1719047347.mp4
ERROR: unable to download video data: [WinError 2] The system cannot find the file specified: '10 Second Countdown _ After Effects-VBKNoLcj8jA.mp4' -> 'server/data/video1719047347.mp4'
DownloadError because move file
127.0.0.1 - - [22/Jun/2024 16:09:07] "GET /video/download?videoUrl=https://www.youtube.com/watch?v=VBKNoLcj8jA HTTP/1.1" 200 -
```
- Get video:
```
http://127.0.0.1:5000/video-downloaded?filename=video1719040531.mp4

127.0.0.1 - - [22/Jun/2024 16:09:26] "GET /video-downloaded?filename=video1719040531.mp4 HTTP/1.1" 200 -
127.0.0.1 - - [22/Jun/2024 16:09:26] "GET /video-downloaded?filename=video1719040531.mp4 HTTP/1.1" 206 -
```

# References
- [Flask document](https://flask.palletsprojects.com/en/3.0.x/)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
