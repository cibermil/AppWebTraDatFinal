from flask import Flask, render_template, request

app=Flask(__name__, template_folder='templates')


@app.route('/')
def inicio():
    return render_template("index.html")
@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    return render_template("mostrar.html", nombre=nombre, edad=edad)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8000, debug=True)