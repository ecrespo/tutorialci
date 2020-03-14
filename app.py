from flask import Flask

APP = Flask(__name__)


@APP.route("/<name>")
def hello_world(name: str) -> str:
    return hello_name(name)


def hello_name(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    APP.run(debug=False)
