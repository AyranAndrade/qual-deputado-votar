from partidos import partidos

import pymysql

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

for partido in partidos:
    sql = "INSERT INTO partidos(nome_partido) VALUES ('{}')".format(partido)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

db.close()
