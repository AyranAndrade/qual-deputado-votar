import pymysql

from politicos import politicos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

for politico in politicos:
    cursor.execute("SELECT partido_id FROM partidos where nome_partido = '{}'".format(politico['partido']))

    partido_id = cursor.fetchone()[0]

    esta_em_exercicio = politico['exercicio'] == 'sim'

    foto = 'https://especiais.g1.globo.com/politica/2019/o-voto-dos-deputados/images/{}'.format(politico['foto'])

    sql = "INSERT INTO politicos(politico_id, nome_politico, foto, uf, esta_em_exercicio, partido_id) " \
          "VALUES ({}, '{}', '{}', '{}', {}, {})".format(politico['id'],
                                                         politico['nome'],
                                                         foto,
                                                         politico['uf'],
                                                         esta_em_exercicio,
                                                         partido_id)

    print(sql)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        exit(-1)

db.close()
