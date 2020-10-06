import pymysql

from votos import votos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

posicionamentos = set()

for voto in votos:
    posicionamentos.add(voto['voto'])

print(posicionamentos)

for posicionamento in posicionamentos:
    sql = "INSERT INTO posicionamentos(posicionamento) VALUES ('{}')".format(posicionamento)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

db.close()
