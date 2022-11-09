import random

def gera_ajuda(dic):
    erradas=[]
    dic_aux={}
    p=random.randint(1,2)
    
    for a,b in dic['opcoes'].items():
        dic_aux[a]=b
        
    del dic_aux[dic['correta']]
    
    for i in dic_aux.values():
        erradas.append(i)
    random.shuffle(erradas)
    resp='DICA:\nOpções certamente erradas: '+erradas[0]
    if p>1:
        resp+=' | '+erradas[1]
    return resp