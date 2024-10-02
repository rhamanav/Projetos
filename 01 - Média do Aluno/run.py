from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/enviar")
def index():
    return render_template("index.html")

@app.route("/lancar_notas", methods=['POST'])
def lancar_notas():
    nome_aluno = request.form["nome_aluno"]
    primeira_nota = float(request.form["primeira_nota"])
    segunda_nota = float(request.form["segunda_nota"])
    terceira_nota = float(request.form["terceira_nota"])

    media = round((primeira_nota + segunda_nota + terceira_nota) / 3, 1)
    
    resultado = "Aprovado" if media >= 6 else "Reprovado"

    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_aluno};{primeira_nota};{segunda_nota};{terceira_nota}; {media}; {resultado} \n")

    return redirect("/enviar")

@app.route("/ver")
def ver_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for nota in arquivo:
            item = nota.strip().split(';')
            if len(item) == 6:
                notas.append({      
                'nome': item[0],
                'nota1': item[1],
                'nota2': item[2],
                'nota3': item[3],
                'media': item[4],
                'resultado': item[5]
                })    
        else:
                 print(f"Linha inválida: {nota}")    
            

            

    return render_template("ver_notas.html", notas = notas)

app.run(host='127.0.0.1', port=80, debug=True)
