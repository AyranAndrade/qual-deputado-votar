import pymysql

from votos import votos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

for voto in votos:
    cursor.execute("SELECT posicionamento_id FROM posicionamentos where posicionamento = '{}'"
                   .format(voto['voto']))
    posicionamento = cursor.fetchone()[0]

    sql = "INSERT INTO votos(projeto_id, politico_id, posicionamento_id) VALUES ({}, {}, {})" \
        .format(voto['idproposicao'],
                voto['idpolitico'],
                posicionamento)

    print(sql)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        exit(-1)

db.close()

print(len(votos))
