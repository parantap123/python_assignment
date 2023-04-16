def get_financial_data_count_DB(mysql,query,params):
    cur = mysql.connection.cursor()
    cur.execute(query, params)
    total_count = cur.fetchone()[0]
    return total_count

def get_financial_data_DB(mysql,query,params):
    cur = mysql.connection.cursor()
    cur.execute(query, params)
    result = cur.fetchall()
    return result

def get_statistics_data_DB(mysql,query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

def insert_financial_data_DB(mysql,query,params):
    cur = mysql.connection.cursor()
    cur.execute(query, params)
    mysql.connection.commit()
    cur.close()