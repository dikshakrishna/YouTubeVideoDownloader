from flask import Flask, request, render_template, url_for
from pytube import YouTube
import pafy
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/link', methods=['GET', 'POST'])
def link():
    try:
        if request.method == "POST":
            lk = request.form["url_download"]
            ytube = YouTube(lk)
            title = ytube.title
            Length = ytube.length
            if request.form.get("audio"):
                result = pafy.new(lk)
                audio_best_quality = result.getbestaudio()
                #download_Directory = str(Path.home() / "Downloads")
                #audio_best_quality.download(download_Directory)
                #yda=ytube.streams.get_audio_only(subtype="mp3")
                audio_best_quality.download(output_path="C:\\Users\\RELIANCE DIGITAL\\Desktop\\stuffs\\study materials\\ME!!\\")
                return render_template('index.html', Title=title, Result="Audio Downloaded")
            if request.form.get("video"):
                yd = ytube.streams.get_highest_resolution()
                download_Directory = str(Path.home() / "Downloads")
                # yd.download(download_Directory)
                yd.download(output_path="C:\\Users\\RELIANCE DIGITAL\\Desktop\\stuffs\\study materials\\ME!!\\")
                return render_template('index.html', Title=title, Result="Video Downloaded")

            return render_template('index.html', Title=title, Length=Length)
    except Exception:
        return render_template("index.html", Result="Invalid URL")


if __name__ == "__main__":
    app.run(debug=True)