import pymysql

from projetos import projetos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

status_projetos = set()

for projeto in projetos:
    status_projetos.add(projeto['status'])

for status in status_projetos:
    sql = "INSERT INTO status_projetos(status_projeto) VALUES ('{}')".format(status)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

db.close()
