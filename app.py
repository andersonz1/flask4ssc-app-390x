from flask import Flask, render_template
import random

app = Flask(__name__)

# list of puppies images
images = [
    "https://media.giphy.com/media/oJWx7MtpR2qdi/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/QGSEGsTr04bPW/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/35FDT0z35sbiKvYC4d/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/bCUhMdu2r0O3e/giphy-downsized-large.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/SIKe5cA5q3cvTSds0a/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/L5ALYguzXR5rW/giphy-downsized-large.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/h7KeaKKxlZntSEpU1d/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
    "https://media.giphy.com/media/PSqg3KBIGbdSMWj5XL/giphy.gif?downsize=715:*&output-format=auto&output-quality=auto",
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
