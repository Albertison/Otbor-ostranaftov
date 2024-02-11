from flask import Flask

app = Flask(__name__)


@app.route("/")
def manu():
    with open("previos.html", "r", encoding='utf-8') as htm_code:
        return htm_code.read()


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
