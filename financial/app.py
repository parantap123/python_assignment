from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from datetime import datetime , timedelta
import os
import requests
import constants
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from get_raw_data import add_data_to_db
from utils import calculate_statistics,create_obj_financial_data, check_date_format , check_number_string,check_if_None
from queries import get_financial_data_count_query_params,get_financial_data_query_params,get_statistics_query
from database_operations import get_financial_data_count_DB, get_financial_data_DB, get_statistics_data_DB

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQL_DATABASE']

mysql = MySQL(app)


def add_data(symbol,variable_dict,start_date,end_date,url):
    response = requests.get(url)
    data_IBM = response.json()[variable_dict["time_series_daily"]]
    logger.info("fetched the " + symbol + " data from the API")
    for date, value in data_IBM.items():
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        if date_obj.date() >= start_date.date() and date_obj.date() <= end_date.date():
            add_data_to_db(mysql,symbol,date,value[variable_dict["open_price"]], value[variable_dict["close_price"]],value[variable_dict["volume"]])    
    logger.info("inserted the " + symbol + " data successfully into the financial_data table")

def get_data():
    start_date = datetime.today() - timedelta(days=14)
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    variable_dict = constants.VARIABLE_DICT
    add_data(constants.IBM_SYMBOL,variable_dict,start_date,end_date,constants.IBM_URL)    
    add_data(constants.APPLE_SYMBOL,variable_dict,start_date,end_date,constants.APPLE_URL)
    logger.info("fetched the all data from API and inserted the data successfully into the financial_data table")
    return {"message":"data added successfully"}

@app.route('/api/fetch_data')
def fetch_data():
    data = get_data()
    return {"data":data}



@app.route('/api/financial_data', methods=['GET'])
def get_financial_data():
    try:
        start_date = request.args.get('start_date')
        check_date_format(start_date,"start_date")
        logger.info("correct format for start_date = " + start_date)
        
        end_date = request.args.get('end_date')
        check_date_format(end_date,"end_date")
        logger.info("correct format for end_date = " + end_date)
        
        symbol = request.args.get('symbol')
        
        limit = request.args.get('limit')
        check_number_string(limit,"limit")
        logger.info("correct type for limit = " + str(limit))
        
        
        page = request.args.get('page')
        check_number_string(page,"page")
        logger.info("correct type for page = " + str(page))
        
        limit = request.args.get('limit', default=5, type=int)
        page = request.args.get('page', default=1, type=int)

        (query,params) = get_financial_data_count_query_params(start_date,end_date,symbol)# this will get the query and the params required for that query to count the total number of records satisfying the query
        logger.info("query and params generated for  getting the financial_data total count")
        total_count = get_financial_data_count_DB(mysql,query,params) # this will return total number of records for that query
        logger.info("total_count for the financial_data is fetched successfully")
        
        (query,params) = get_financial_data_query_params(start_date,end_date,symbol,page,limit)# this will get the query and the params required for that query to return records satisfying the query with pagination
        logger.info("query and params generated for  getting the financial_data")
        result = get_financial_data_DB(mysql,query,params)# this will return records satisfying the query with pagination
        logger.info("financial_data is fetched successfully")

        (processed_data,pagination_obj,info_obj) = create_obj_financial_data(result,total_count,page,limit)# this returns processed data,pagination and the info as perr the requirements
        logger.info("results are processed according to the requirement of the task")
        return {
            'data': processed_data,
            'pagination': pagination_obj,
            'info': info_obj
        }
    except Exception as e:
        logger.error("the error is " + str(e))
        return {
            'data': [],
            'pagination': [],
            'info': {'error': str(e)}
        }

    

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    try:
        start_date = request.args.get('start_date')
        check_if_None(start_date,"start_date")
        check_date_format(start_date,"start_date")
        logger.info("correct format and its not None for start_date = " + start_date)
        
        end_date = request.args.get('end_date')
        check_if_None(end_date,"end_date")
        check_date_format(end_date,"end_date")
        logger.info("correct format and its not None for end_date = " + end_date)
        
        symbol = request.args.get('symbol')
        check_if_None(symbol,"symbol")
        logger.info("symbol is not None and symbol = " + symbol)
        
        query = get_statistics_query(start_date,end_date,symbol) # to generate the query for retriving the data to calculate the statistics
        logger.info("query generated to get the statistics = ") 
        
        data = get_statistics_data_DB(mysql,query)
        logger.info("retrived the data to calculate statistics successfully") # to execute the query for retriving the data to calculate the statistics
        
        (statistics_data,info) = calculate_statistics(data,start_date,end_date,symbol) # to calculate the statistics for the data retrived 
        logger.info("calculated statistics successfully") 
        return {"data":statistics_data, "info":info}
    except Exception as e:
        return {
            'data': [],
            'info': {'error': str(e)}
        }


    
    

if __name__ == '__main__':
    # get_data()
    app.run(host='0.0.0.0',port=5004)
