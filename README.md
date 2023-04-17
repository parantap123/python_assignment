# Description
This project is a financial data analysis  application that retrieves stock market data from AlphaVantage API and stores it in a MySQL database. The application is built using Python and the Flask web framework. The application allows users to query the stored financial data through a set of RESTful APIs.

Key features of the project include:

Retrieval of historical financial data from AlphaVantage API for specific stock symbols (IBM and Apple Inc.).<br />
Storage of the retrieved data in a MySQL database using Docker Compose for easy setup and deployment.<br />
Implementation of APIs to fetch financial data and perform statistical analysis within specified date ranges and stock symbols.<br />
Error handling and logging to ensure smooth operation and easier debugging.<br />

# Tech stack 
Python: The programming language used for the entire project.<br />
Flask: A lightweight web framework for building API services in Python.<br />
Flask-MySQLdb: A Flask extension that provides a simple interface for connecting to MySQL databases.<br />
MySQL: The relational database management system used for storing data.<br />
Docker: A platform for developing, shipping, and running applications in containers.<br />
Docker Compose: A tool for defining and running multi-container Docker applications.<br />
In addition to these, I am also using the requests library for making HTTP requests to the AlphaVantage API, and datetime for handling date and time operations.<br />

# steps to run the code in the local enviroment
run this ```docker-compose up --build``` in the mail directory of the project where docker-compose.yml is present

## Task1
This task will do the following: 
1. fetch the data from  AlphaVantage API for specific stock symbols (IBM and Apple Inc.) for the last 2 weeks <br />
2. process the data and insert it into the financial_data table

### The way to use the API:
```curl -X POST  'http://127.0.0.1:5004/api/fetch_data'```
This was done as an API as it would make it easier for the evaluater to run the API multiple times tro check if the duplicate records are inserted into the DB

## Task2

### part 1
 This task will do the following 
 1. retrieve records from financial_data table with paramentres **start_date**, **end_date**, **symbol**, **limit** and **page**  all the parametres are **optional** if limit is not given then the default values is taken to be 5 and if page is not given then the default values is taken to be 1.
 2. It will provide the data , pagination and info 
#### The way to use the API:
```curl -X GET 'http://localhost:5004/api/financial_data?start_date=2023-04-10&end_date=2023-04-14&page=1&limit=2'```






 


## Task2
### Problem Statement:
1. Implement an Get financial_data API to retrieve records from `financial_data` table, please note that:
    - the endpoint should accept following parameters: start_date, end_date, symbol, all parameters are optional
    - the endpoint should support pagination with parameter: limit and page, if no parameters are given, default limit for one page is 5
    - the endpoint should return an result with three properties:
        - data: an array includes actual results
        - pagination: handle pagination with four properties
            
            - count: count of all records without panigation
            - page: current page index
            - limit: limit of records can be retrieved for single page
            - pages: total number of pages
        - info: includes any error info if applies
    

Sample Request:
```bash
curl -X GET 'http://localhost:5000/api/financial_data?start_date=2023-01-01&end_date=2023-01-14&symbol=IBM&limit=3&page=2'

```
Sample Response:
```
{
    "data": [
        {
            "symbol": "IBM",
            "date": "2023-01-05",
            "open_price": "153.08",
            "close_price": "154.52",
            "volume": "62199013",
        },
        {
            "symbol": "IBM",
            "date": "2023-01-06",
            "open_price": "153.08",
            "close_price": "154.52",
            "volume": "59099013"
        },
        {
            "symbol": "IBM",
            "date": "2023-01-09",
            "open_price": "153.08",
            "close_price": "154.52",
            "volume": "42399013"
        }
    ],
    "pagination": {
        "count": 20,
        "page": 2,
        "limit": 3,
        "pages": 7
    },
    "info": {'error': ''}
}

```

2. Implement an Get statistics API to perform the following calculations on the data in given period of time:
    - Calculate the average daily open price for the period
    - Calculate the average daily closing price for the period
    - Calculate the average daily volume for the period

    - the endpoint should accept following parameters: start_date, end_date, symbols, all parameters are required
    - the endpoint should return an result with two properties:
        - data: calculated statistic results
        - info: includes any error info if applies

Sample request:
```bash
curl -X GET http://localhost:5000/api/statistics?start_date=2023-01-01&end_date=2023-01-31&symbol=IBM

```
Sample response:
```
{
    "data": {
        "start_date": "2023-01-01",
        "end_date": "2023-01-31",
        "symbol": "IBM",
        "average_daily_open_price": 123.45,
        "average_daily_close_price": 234.56,
        "average_daily_volume": 1000000
    },
    "info": {'error': ''}
}

```

## What you should deliver:
Directory structure:
```
project-name/
├── model.py
├── schema.sql
├── get_raw_data.py
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── financial/<Include API service code here>

```

1. A `get_raw_data.py` file in root folder

    Action: 
    
    Run 
    ```bash
    python get_raw_data.py
    ```

    Expectation: 
    
    1. Financial data will be retrieved from API and processed,then insert all processed records into table `financial_data` in local db
    2. Duplicated records should be avoided when executing get_raw_data multiple times, consider implementing your own logic to perform upsert operation if the database you select does not have native support for such operation.

2. A `schema.sql` file in root folder
    
    Define schema for financial_data table, if you prefer to use an ORM library, just **ignore** this deliver item and jump to item3 below.

    Action: Run schema definition in local db

    Expectation: A new table named `financial_data` should be created if not exists in db

3. (Optional) A `model.py` file: 
    
    If you perfer to use a ORM library instead of DDL, please include your model definition in `model.py`, and describe how to perform migration in README.md file

4. A `Dockerfile` file in root folder

    Build up your local API service

5. A `docker-compose.yml` file in root folder

    Two services should be defined in docker-compose.yml: Database and your API

    Action:

    ```bash
    docker-compose up
    ```

    Expectation:
    Both database and your API service is up and running in local development environment

6. A `financial` sub-folder:

    Put all API implementation related codes in here

7. `README.md`: 

    You should include:
    - A brief project description
    - Tech stack you are using in this project
    - How to run your code in local environment
    - Provide a description of how to maintain the API key to retrieve financial data from AlphaVantage in both local development and production environment.

8. A `requirements.txt` file:

    It should contain your dependency libraries.

## Requirements:

- The program should be written in Python 3.
- You are free to use any API and libraries you like, but should include a brief explanation of why you chose the API and libraries you used in README.
- The API key to retrieve financial data should be stored securely. Please provide a description of how to maintain the API key from both local development and production environment in README.
- The database in Problem Statement 1 could be created using SQLite/MySQL/.. with your own choice.
- The program should include error handling to handle cases where the API returns an error or the data is not in the correct format.
- The program should cover as many edge cases as possible, not limited to expectations from deliverable above.
- The program should use appropriate data structures and algorithms to store the data and perform the calculations.
- The program should include appropriate documentation, including docstrings and inline comments to explain the code.

## Evaluation Criteria:

Your solution will be evaluated based on the following criteria:

- Correctness: Does the program produce the correct results?
- Code quality: Is the code well-structured, easy to read, and maintainable?
- Design: Does the program make good use of functions, data structures, algorithms, databases, and libraries?
- Error handling: Does the program handle errors and unexpected input appropriately?
- Documentation: Is the code adequately documented, with clear explanations of the algorithms and data structures used?

## Additional Notes:

You have 7 days to complete this assignment and submit your solution.
