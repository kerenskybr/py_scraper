#Funcao para remover linhas que iniciem com um dado valor

def removeValores(arquivoEntrada, arquivoSaida):

    input = open(arquivoEntrada, "r")
    output = open(arquivoSaida, "w")

    output.write(input.readline())

    for line in input:
        if not line.lstrip().startswith("0"):
            output.write(line)

    input.close()
    output.close()

removeValores('csv_osorio_limpo.csv', 'csv_final.csv')