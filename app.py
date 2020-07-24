#https://levelup.gitconnected.com/10-tools-i-use-to-craft-better-python-code-b9a9776a7871
from flask import Flask

APP = Flask(__name__)


@APP.route("/<nombre>")
def hola_mundo(nombre: str) -> str:
    return hola_nombre(nombre)


def hola_nombre(nombre: str) -> str:
    return f"hola, {nombre}"


if __name__ == "__main__":
    APP.run(debug=False)
