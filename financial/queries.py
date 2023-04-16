#depending on the paramentres present it adds the conditions
def get_conditions(start_date,end_date,symbol):
    conditions = []
    if start_date:
        conditions.append('date1 >= %s')
    if end_date:
        conditions.append('date1 <= %s')
    if symbol:
        conditions.append('symbol = %s')
    return conditions

#it generates the query and param to count the financial data
def get_financial_data_count_query_params(start_date,end_date,symbol):
    query = 'SELECT COUNT(*) FROM financial_data WHERE '
    conditions = get_conditions(start_date,end_date,symbol)
    if not conditions:
        query = 'SELECT COUNT(*) FROM financial_data'
        params = ()
    else:
        query += ' AND '.join(conditions)
        params = tuple(filter(None, [start_date, end_date, symbol]))
        
    return (query,params)

#it generates the query and param to get the financial data with pagination
def get_financial_data_query_params(start_date,end_date,symbol,page,limit):
    offset = (page - 1) * limit
    query = 'SELECT * FROM financial_data WHERE '
    conditions = get_conditions(start_date,end_date,symbol)
    if not conditions:
        query = 'SELECT * FROM financial_data'
        params = ()
    else:
        query += ' AND '.join(conditions)
        params = tuple(filter(None, [start_date, end_date, symbol]))
    query += f' LIMIT {limit} OFFSET {offset}'
    return (query,params)

#it generates the query and params to insert the data into the financial_data table
def get_insert_financial_data_query_params(symbol,date1,open_price,close_price,volume):
    query = "INSERT IGNORE INTO financial_data (symbol, date1,open_price, close_price, volume) VALUES (%s, %s,%s,%s,%s)"
    params = (symbol, date1, open_price, close_price, volume)
    return (query,params)

#it generates the query to get the statistics
def get_statistics_query(start_date,end_date,symbol):
    query = f"SELECT * FROM financial_data WHERE date1 BETWEEN '{start_date}' AND '{end_date}' AND symbol = '{symbol}'"
    return query
    
    
