from flask import Flask


@app.route("/<name>")
def hello_world(name: str) -> str:
    return hello_name(name)


def hello_name(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    app = Flask(__name__)
    app.run(debug=False)
