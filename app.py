from flask import Flask, send_from_directory, send_file,request, render_template
import make_pasta
app = Flask(__name__, template_folder="public")
@app.route("/")
def index():
    return render_template("index.html", data="", input="")
@app.route('/<path:path>')
def send(path):
    return send_from_directory('public', path)
@app.route("/translate", methods=["POST"])
def translate():
    text = request.form['v']
    out = make_pasta.translate(text)
    return render_template("index.html", data=out, input=request.form['v'])