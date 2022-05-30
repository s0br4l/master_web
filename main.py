from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/registrosdiarios')
def registrosdiarios():
    return render_template("registrosdiarios.html")

@app.route('/analises')
def analises():
    return render_template("analises.html")


if __name__ == "__main__":
    app.run()
