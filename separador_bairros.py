#Funcao para remover linhas que iniciem com um dado valor

def removeValores(arquivoEntrada, arquivoSaida):

    input = open(arquivoEntrada, "r")
    output = open(arquivoSaida, "w")

    output.write(input.readline())

    for line in input:
        if "centro" in line:
            output.write(line)

    input.close()
    output.close()

removeValores('new_data_bkp.csv', 'centro.csv')