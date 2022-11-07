def questao_para_texto(dic, n):
    resp='{2}\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\n'.format(n, dic['titulo'],'-'*40)
    for a,b in dic['opcoes'].items():
        resp+='{0}: {1}\n'.format(a, b)
    return resp