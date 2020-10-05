import pymysql

from projetos import projetos

db = pymysql.connect("localhost", "newuser", "", "qual_deputado_votar")

cursor = db.cursor()

tipos_turno = set()

for projeto in projetos:
    tipos_turno.add(projeto['turno'])

for tipo_turno in tipos_turno:
    if tipo_turno == '1':
        tipo = 'primeiro'
    elif tipo_turno == '2':
        tipo = 'segundo'
    else:
        tipo = 'unico'

    sql = "INSERT INTO tipos_turno(tipo_turno) VALUES ('{}')".format(tipo)

    try:
        cursor.execute(sql)

        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

db.close()
