def transforma_base(lista):
    dic2 = {}
    for i in range(len(lista)):
        dic = lista[i]
        if dic['nivel'] == 'facil':
            if dic['nivel'] in dic2.keys():
                lista1.append(dic)
                dic2[dic['nivel']] = lista1
            else:
                lista1= []
                lista1.append(dic)
                dic2[dic['nivel']] = lista1

        if dic['nivel'] == 'medio':
            if dic['nivel'] in dic2.keys():
                lista2.append(dic)
                dic2[dic['nivel']] = lista2
            else:
                lista2= []
                lista2.append(dic)
                dic2[dic['nivel']] = lista2

        if dic['nivel'] == 'dificil':
            if dic['nivel'] in dic2.keys():
                lista3.append(dic)
                dic2[dic['nivel']] = lista3
            else:
                lista3= []
                lista3.append(dic)
                dic2[dic['nivel']] = lista3

    return dic2
