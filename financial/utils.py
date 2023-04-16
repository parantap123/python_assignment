from math import ceil
from datetime import datetime , timedelta
def calculate_statistics(data,start_date,end_date,symbol):
    total_daily_open_price = 0
    total_daily_close_price = 0
    total_daily_volume = 0
    average_daily_open_price = 0
    average_daily_close_price = 0
    average_daily_volume = 0
    info = {}
    statistics_data = {"start_date":start_date,"end_date":end_date,"symbol":symbol,"average_daily_open_price":average_daily_open_price,"average_daily_close_price":average_daily_close_price,"average_daily_volume":average_daily_volume}
    
    #check if the data is not empty if its empty then the averages are 0
    if(len(data) == 0):
        info = {"error":"there is no data with the query so there the averages are 0"}
        return (statistics_data,info)
    
    #summing all the values 
    for day_data in data:
        total_daily_open_price += day_data[2]
        total_daily_close_price += day_data[3]
        total_daily_volume += day_data[4]
    
    #calculating the average sum / total_elements
    average_daily_open_price = total_daily_open_price / len(data)
    average_daily_close_price = total_daily_close_price / len(data)
    average_daily_volume = total_daily_volume / len(data)
    statistics_data = {"start_date":start_date,"end_date":end_date,"symbol":symbol,"average_daily_open_price":average_daily_open_price,"average_daily_close_price":average_daily_close_price,"average_daily_volume":average_daily_volume}
    
    return (statistics_data,info)

# this changes the format of the date according to the requirement
def change_date_format(date_obj):
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date
    


# this is util function to prepare the response data as per the requirement
def create_obj_financial_data(data_set,count,page,limit):
    processed_data = []
    for  data in data_set:
        current_processed_obj = {"symbol":data[0], "date":change_date_format(data[1]),"open_price":data[2], "close_price": data[3], "volume":data[4]}
        processed_data.append(current_processed_obj)
    pages = ceil(count/(limit * 1.0))
    pagination_obj = {"count":count, "page":page, "limit":limit,"pages":pages}
    info_obj = {'error': ''}
    return (processed_data,pagination_obj,info_obj)

# this function is used for the error handling of the date paremetres
def check_date_format(date_string,date_variable):
    try:
        if date_string is None:
            return
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        print("Date string is valid date format.")
    except Exception as e:
        raise Exception(date_variable + " is not in correct date format")

# this function is used for the error handling of the number paremetres
def check_number_string(variable,variabe_name):
    try:
        if variable is None:
            return
        int_limit = int(variable)
    except Exception as e:
        # Handle the error here
         raise Exception(variabe_name + " is not a number")

# this function is used for the error handling of the required paremetres
def check_if_None(variable,variabe_name):
    try:
        if variable is None:
            raise Exception(variabe_name + " is a required parametre")
    except Exception as e:
        # Handle the error here
         raise Exception(str(e))
    
        
        
    
    

    