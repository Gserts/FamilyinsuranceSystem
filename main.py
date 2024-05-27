import pymysql

# Database Parameters
db = pymysql.connect(host='gz-cynosdbmysql-grp-79rn9tub.sql.tencentcdb.com',
                     port=26791,
                   user='root',
                   password='Zsc85621362',
                   database='Project',
                   charset='utf8')
# Cursor of database
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print('Link Successfully')
db.close()