from flask import Flask, jsonify, request
from queries import get_insert_financial_data_query_params
from database_operations import insert_financial_data_DB
def add_data_to_db(mysql,symbol,date1,open_price,close_price,volume):
    (query,params) = get_insert_financial_data_query_params(symbol,date1,open_price,close_price,volume)
    insert_financial_data_DB(mysql,query,params)
    return jsonify({"message": "data added successfully"})
