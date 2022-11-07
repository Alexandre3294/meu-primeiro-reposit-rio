import random 
def sorteia_questao(dic,nivel):
    return random.choice(dic[nivel])
def sorteia_questao_inedida(dic_quests,nivel, sort):
    q_resp=sorteia_questao(dic_quests,nivel)
    while q_resp in sort:
        q_resp=sorteia_questao(dic_quests,nivel)
    sort.append(q_resp)
    return q_resp