from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    imgs = []
    if os.path.exists("alerts"):
        imgs = sorted(os.listdir("alerts"), reverse=True)
    return render_template("index.html", images=imgs)

@app.route("/alerts/<f>")
def img(f):
    return send_from_directory("alerts", f)

if __name__ == "__main__":
    app.run(debug=True)