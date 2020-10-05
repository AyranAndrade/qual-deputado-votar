import pymysql

from projetos import projetos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

print(len(projetos))

for projeto in projetos:
    cursor.execute("SELECT status_projeto_id FROM status_projetos where status_projeto = '{}'"
                   .format(projeto['status']))
    status_projeto = cursor.fetchone()[0]

    partes = projeto['data_votacao'].split(sep='/')
    data_votacao = partes[2] + '-' + partes[1] + '-' + partes[0]

    if projeto['turno'] == '1':
        tipo = 'primeiro'
    elif projeto['turno'] == '2':
        tipo = 'segundo'
    else:
        tipo = 'unico'

    cursor.execute("SELECT tipo_turno_id FROM tipos_turno where tipo_turno = '{}'".format(tipo))
    tipo_turno = cursor.fetchone()[0]

    resumo = projeto['resumo'].replace('\'', '')

    sql = "INSERT INTO projetos(titulo, data_votacao, quorum_minimo, resumo, link_noticia, status_projeto_id, " \
          "tipo_turno_id) " \
          "VALUES ('{}', '{}', {}, '{}', '{}', {}, {})".format(projeto['vulgar'],
                                                               data_votacao,
                                                               projeto['quorum_minimo'],
                                                               resumo,
                                                               projeto['link_g1'],
                                                               status_projeto,
                                                               tipo_turno)

    print(sql)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

db.close()
