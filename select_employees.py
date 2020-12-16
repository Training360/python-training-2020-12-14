import mariadb

cnx = mariadb.connect(user='employees', database='employees', password="employees")
cursor = cnx.cursor()
cursor.execute("select name, year from employees")
for (name, year) in cursor:
    print(name + " - " + str(year))
cursor.close()
cnx.close()