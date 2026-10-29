from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Enviamos una variable al HTML
    return render_template('index.html', mensaje="¡Hola estudiantes de Programación!")

if __name__ == '__main__':
    app.run(debug=True)
