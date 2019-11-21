def calculo_juros(investimento,porce):
    calculo_juros=investimento*((1+porce)**12)#calcula por 12 meses 12*
    return calculo_juros


def lucro(investimento,calculo_juros):
    lucro=calculo_juros-investimento#calcula o lucro obtido
    return lucro