import json

import pymysql

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

# projeto_id: 1 para sim, 0 para não
meus_posicionamentos = {
    1: 1,
    2: 0,
    4: 0,
    5: 1,
    6: 0,
    7: 1,
    11: 1,
    12: 1,
    13: 1,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    20: 1,
    21: 0,
    22: 0,
    25: 1,
    28: 0,
    32: 0,
    35: 1,
    37: 1,
    44: 1,
    48: 1,
    52: 0,
    53: 1,
    55: 0,
    56: 1,
    59: 1,
    61: 1,
}

ranking_politicos = []

cursor.execute("SELECT politico_id, nome_politico, uf, esta_em_exercicio, nome_partido FROM politicos po "
               "inner join partidos pa on po.partido_id = pa.partido_id")
politicos = cursor.fetchall()

for politico in politicos:
    cursor.execute("SELECT projeto_id, politico_id, posicionamento from votos v inner join posicionamentos p "
                   "on v.posicionamento_id = p.posicionamento_id where politico_id = {}"
                   .format(politico[0]))
    votos = cursor.fetchall()

    for voto in votos:
        if voto[0] in meus_posicionamentos:
            posicionamento_politico = 1 if voto[2] == 'sim' else 0
            meu_posicionamento = meus_posicionamentos[voto[0]]

            if meu_posicionamento == posicionamento_politico:
                ranking = next((x for x in ranking_politicos if politico[0] == x['id']), {
                    'id': politico[0],
                    'nome': politico[1],
                    'uf': politico[2],
                    'exercicio': politico[3],
                    'partido': politico[4],
                    'pontuacao': 0
                })

                if ranking not in ranking_politicos:
                    ranking_politicos.append(ranking)

                ranking['pontuacao'] = ranking['pontuacao'] + 1
            else:
                ranking = next((x for x in ranking_politicos if politico[0] == x['id']), {
                    'id': politico[0],
                    'nome': politico[1],
                    'uf': politico[2],
                    'exercicio': politico[3],
                    'partido': politico[4],
                    'pontuacao': 0
                })

                if ranking not in ranking_politicos:
                    ranking_politicos.append(ranking)

                ranking['pontuacao'] = ranking['pontuacao'] - 1

ranking_politicos.sort(key=lambda x: x['pontuacao'], reverse=True)
print(json.dumps(ranking_politicos, indent=4))
