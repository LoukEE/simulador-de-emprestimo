from flask import Flask, render_template, request

app = Flask(__name__)



def validar(valor_emprestimo, renda_mensal): 
    emprestimo_maximo = renda_mensal * 45/100
    if  valor_emprestimo > emprestimo_maximo:
        return False
    else:
        return True

def calcular(valor_emprestimo, prazo):
    taxa = 0.02

    prestacao = (valor_emprestimo * taxa)/(1 - (1+taxa)** -prazo)
    total = prestacao*prazo
    return prestacao,taxa, total

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        renda_mensal = float(request.form['renda_mensal'])
        valor_emprestimo = float(request.form['valor_emprestimo'])
        prazo = int(request.form['prazo'])

        if not validar(valor_emprestimo, renda_mensal):
            return render_template('index.html',message='O valor solicitado não está entre \
                 as condições necessárias para a realização do emprestimo. (O valor de emprestimo\
                 não pode ultrapassar 45% da sua renda mensal)')


        prestacao, taxa, total = calcular(valor_emprestimo, prazo)

        return render_template('result.html', prestacao=prestacao, taxa=taxa,total=total, valor_emprestimo=valor_emprestimo)
    return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True)
    


