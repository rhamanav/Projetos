from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    condicao = None
    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        imc = peso / (altura ** 2)
        resultado = round(imc, 2)

        if imc < 18.5:
            condicao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            condicao = "Peso normal"
        elif 25 <= imc < 29.9:
            condicao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            condicao = "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            condicao = "Obesidade grau 2"
        else:
            condicao = "Obesidade grau 3"
   
    return render_template("index.html", resultado=resultado, condicao=condicao)
   
 
 
app.run("127.0.0.1", port=80, debug=True)