from flask import Flask, render_template, request
import jieba

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/getResult", methods=["POST"])
def getResult():
    source = request.form.get("source")
    words = jieba.cut(source)
    return "/".join(words)

if __name__ == '__main__':
    app.run()
