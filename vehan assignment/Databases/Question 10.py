import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "system",
    database = "university"
)

print(db)
cursor = db.cursor()
# cursor.execute("CREATE table student(id int(1) auto_increment primary key,name varchar(20),grade float);")

cursor.execute("INSERT INTO student(name, grade) VALUES('Sagar', 8.9);")

db.commit()