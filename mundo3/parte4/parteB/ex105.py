def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n)/ len(n)
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['média'] >=5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno
                             

# Programa Principal
resp = notas(5.5, 6.5, 10, 6.5)
print(resp)
#help(notas)
