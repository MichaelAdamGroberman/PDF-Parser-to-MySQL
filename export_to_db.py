import mysql.connector

def export_data_to_mysql(host, database, user, password, data):
    # establish the connection
    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    cursor = cnx.cursor()

    add_data_query = ("INSERT INTO TableName "
                   "(ColumnName) "
                   "VALUES (%s)")
    cursor.execute(add_data_query, (data,))

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
