from flask import Flask, render_template, request
from consultadb import BuscarDatos

app=Flask(__name__, template_folder='templates')


@app.route('/')
def inicio():
    return render_template("index.html")
@app.route('/procesar', methods=['POST'])
def procesar():
    desvehiculofun = request.form.get("desvehiculo")
    aniofun = request.form.get("anio")
    #request.values.get["desvehiculo"]

    encontrado=BuscarDatos(desvehiculo=desvehiculofun,anio=aniofun,verbose=True)

    return render_template("mostrar.html",datos=encontrado)
    #return render_template("mostrar.html", desvehiculo=desvehiculomos, anio=aniomos)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)