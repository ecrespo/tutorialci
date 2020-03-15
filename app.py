from flask import Flask

app = Flask(__name__)

@app.route('/<nombre>')
def hola_mundo(nombre: str) -> str:
    return hola_nombre(nombre)

def hola_nombre(nombre: str) -> int:
    return f"hola, {nombre}"

if __name__ == '__main__':
    app.run(debug=True)