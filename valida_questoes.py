def valida_questao(dic1):
    resp={}
    if list(dic1.keys()) != ['titulo','nivel','opcoes','correta']:
        if 'titulo' not in list(dic1.keys()):
            resp['titulo']='nao_encontrado'
        if 'nivel' not in list(dic1.keys()):
            resp['nivel']='nao_encontrado'
        if 'opcoes' not in list(dic1.keys()):
            resp['opcoes']='nao_encontrado'
        if 'correta' not in list(dic1.keys()):
            resp['correta']='nao_encontrado'
    if len(dic1.keys()) != 4:
        resp['outro']='numero_chaves_invalido'
    if 'titulo' in list(dic1.keys()):
        if dic1['titulo'] == '\t' or dic1['titulo'] == '':
            resp['titulo']='vazio'
    if 'nivel' in list(dic1.keys()):
        if dic1['nivel'] != 'facil':
            if dic1['nivel'] != 'medio':
                if dic1['nivel'] != 'dificil':
                    resp['nivel']='valor_errado'
    if 'opcoes' in list(dic1.keys()):    
        opcoes = dic1['opcoes']
        if len(opcoes.keys()) == 4:
            if list(opcoes.keys()) == ['A', 'B', 'C', 'D']:
                if opcoes['A'] == '\t' or opcoes['A'] ==''  or opcoes['B'] == '\t' or opcoes['B'] ==''  or opcoes['C'] == '\t' or opcoes['C'] ==''  or opcoes['D'] == '\t' or opcoes['D'] == '':
                    dic2={}
                    if opcoes['A'] == '\t' or opcoes['A'] == '':
                        dic2['A']='vazia'
                    if opcoes['B'] == '\t' or opcoes['B'] == '':
                        dic2['B']='vazia'
                    if opcoes['C'] == '\t' or opcoes['C'] == '':
                        dic2['C']='vazia'
                    if opcoes['D'] == '\t' or opcoes['D'] == '':
                        dic2['D']='vazia'
                    resp['opcoes']=dic2
            else:
                resp['opcoes']='chave_invalida_ou_nao_encontrada'
        else:
            resp['opcoes']='tamanho_invalido'
    if 'correta' in list(dic1.keys()):    
        if dic1['correta'] not in ['A', 'B', 'C', 'D']:
            resp['correta']='valor_errado'
    return resp

def valida_questoes(lista):
    resp=[]
    for d in lista:
        probs=valida_questao(d)
        resp.append(probs)
    return resp