#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas                                                                                                                                                  – A maior nota                                                                                                                                                                – A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      – A situação (opcional)

def notas(*valores, sit = False):
    """
        -> Função para analisar notas e situações de vários alunos
        :param nota: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    dic={}
    dic["total"]= len(valores)
    dic["maximo"]= max(valores)
    dic["minimo"]= min(valores)
    dic["media"]= sum(valores)/ len(valores)

    if sit:
        if dic["media"] > 7:
            dic["Situacao"]= "Boa"
        
        elif dic["media"] >= 5:
            dic["Situacao"] = "Razoavel"
        
        else:
            dic["Situacao"] = "Ruim"
    return dic