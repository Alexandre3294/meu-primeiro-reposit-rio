def questao_para_texto(dic, n):
    resp='QUESTAO {0}\n\n{1}\n\nRESPOSTAS:\n'.format(n, dic['titulo'])
    for a,b in dic['opcoes'].items():
        resp+='{0}: {1}\n'.format(a, b)
    return resp