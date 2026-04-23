from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Vértice: Onde o topo encontra a confiança.</h1><p>O MVP está online!</p>"

if __name__ == '__main__':
    app.run(debug=True)