from __future__ import unicode_literals
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
import youtube_dl

import os
import shutil

from time import time 


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/myvideo")
def myvideo():
    return render_template("index.html")


@app.route("/video-url")
def getVideoUrl():
    return send_from_directory("static", "video/video.mp4")

@app.route("/video/download")
def downloadVideo():
    videoUrl = request.args.get("videoUrl", "")
    # app.logger.debug('videoUrl' + videoUrl)
    print('videoUrl' + videoUrl)
    
    if (videoUrl != "") :
        try:
            ydl_opts = {
                'progress_hooks': [download_hook],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([videoUrl])
        except youtube_dl.utils.DownloadError:
            print('DownloadError because move file')

    return "<p>Downloading!</p>"

def download_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        
        oldFilename = d['filename']
        newFilename = "video" + str(int(time())) + ".mp4"
        
        print('oldFilename ' + oldFilename)
        print('newFilename ' + newFilename)
        
        os.rename(oldFilename, "server/data/"+ newFilename)
        os.replace(oldFilename, "server/data/"+ newFilename)
        shutil.move(oldFilename, "server/data/"+ newFilename)

@app.route("/video-downloaded")
def getVideoDownload():
    filename = request.args.get("filename", "")
    return send_from_directory("data", filename)