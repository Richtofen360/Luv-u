from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        try:
            # Obtener los números y la operación desde el formulario
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]
            
            # Realizar el cálculo
            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error: División por cero"
        except ValueError:
            resultado = "Error: Entrada no válida"
    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
