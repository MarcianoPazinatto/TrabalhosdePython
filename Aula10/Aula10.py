#---Aula 10 web
#---WEB  - CALCULADORA
nome_pagina = 'Calculadora Python'

from flask import Flask, render_template, request
from calculos import*
app = Flask (__name__)

@app.route('/')

def home():
    return render_template('home.html',titulo=nome_pagina)

@app.route('/Calcular')
def Calculadora():
    num1=int(request.args['numero1'])
    num2=int(request.args['numero2'])
    
    rsoma=soma(num1,num2)
    rsub=sub(num1,num2)
    rmult=mult(num1,num2)
    rdiv_inteira=div_inteira(num1,num2)
    rdiv_fra=div_fra(num1,num2)
    rresto=resto(num1,num2)
    rraiz=raiz(num1,num2)
    resultados={'soma':rsoma,'sub':rsub,'mult':rmult,'div_inteira':rdiv_inteira,'div_fra':rdiv_fra,'resto':rresto, 'raiz':rraiz}
    
    return render_template('resultado.html',num1=num1,num2=num2, resultados=resultados)
app.run(debug=True)