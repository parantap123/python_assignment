# Description
This project is a financial data analysis  application that retrieves stock market data from AlphaVantage API and stores it in a MySQL database. The application is built using Python and the Flask web framework. The application allows users to query the stored financial data through a set of RESTful APIs. The API is containerized using Docker, making it easy to run and manage without needing to install any additional dependencies, except for Docker Engine itself.

Key features of the project include:

Retrieval of historical financial data from AlphaVantage API for specific stock symbols (IBM and Apple Inc.).<br />
Storage of the retrieved data in a MySQL database using Docker Compose for easy setup and deployment.<br />
Implementation of APIs to fetch financial data and perform statistical analysis within specified date ranges and stock symbols.<br />
Error handling and logging to ensure smooth operation and easier debugging.<br />

# Prerequisites
1. **Docker Engine**

# Tech stack 
**Python** : The programming language used for the entire project.<br />
**Flask**: A lightweight web framework for building API services in Python.<br />
**Flask-MySQLdb**: A Flask extension that provides a simple interface for connecting to MySQL databases.<br />
**MySQL**: The relational database management system used for storing data.<br />
**Docker**: A platform for developing, shipping, and running applications in containers.<br />
**Docker Compose**: A tool for defining and running multi-container Docker applications.<br />
In addition to these, I am also using the requests library for making HTTP requests to the AlphaVantage API, and datetime for handling date and time operations.<br />

# steps to run the code in the local enviroment

To run the project, you don't need to install anything other than Docker Engine. Follow the steps below to run the project:

1. Ensure that Docker Engine is installed on your system. If not, please refer to the official documentation to install Docker Engine. link to the website  https://docs.docker.com/engine/install/ 
2. Clone the repository to your local system.
3. Open a terminal/command prompt and navigate to the project's root directory.
4. Run the following command: ``` docker-compose up --build ```

This command will build the necessary Docker images and start the services defined in the docker-compose.yml file. You don't need to worry about installing any other dependencies or setting up the environment, as Docker will handle everything for you.

Once the containers are up and running, you can access the API at the specified endpoint (e.g., http://127.0.0.1:5004/api/fetch_data). For more information on using the API, please refer to the API documentation in the project.

## Task1
This task will do the following: 
1. fetch the data from  AlphaVantage API for specific stock symbols (IBM and Apple Inc.) for the last 2 weeks <br />
2. process the data and insert it into the financial_data table

### The way to use the API:
```curl -X POST  'http://127.0.0.1:5004/api/fetch_data'```<br />
***please run this API first so as to populate the data in the DB***
This was done as an API as it would make it easier for the evaluater to run the API multiple times to check if the duplicate records are inserted into the DB

## Task2

### part 1
 This task will do the following : <br />
 1. retrieve records from financial_data table with input paramentres **start_date**, **end_date**, **symbol**, **limit** and **page**  all the parametres are **optional**. If limit is not given then the default values is taken to be 5 and if page is not given then the default values is taken to be 1.
 2. It will provide the data , pagination and info 
#### The way to use the API:
```curl -X GET 'http://localhost:5004/api/financial_data?start_date=2023-04-10&end_date=2023-04-14&page=1&limit=2'```

**The sample response will look like:**

```
{
    "data": [
        {
            "close_price": 162.03,
            "date": "2023-04-10",
            "open_price": 161.42,
            "symbol": "Apple Inc.",
            "volume": 47716882
        },
        {
            "close_price": 160.8,
            "date": "2023-04-11",
            "open_price": 162.35,
            "symbol": "Apple Inc.",
            "volume": 47644217
        }
    ],
    "info": {
        "error": ""
    },
    "pagination": {
        "count": 10,
        "limit": 2,
        "page": 1,
        "pages": 5
    }
}

```


### part 2
This task will do the following : <br />
1. This will take paramentres  **start_date**, **end_date**, **symbol** all the parametres are required **required** and will generate the folllowing:
    1. Calculate the average daily open price for the period <br />
    2. Calculate the average daily closing price for the period <br />
    3. Calculate the average daily volume for the period <br />
2. This api will respond with data and info

#### The way to use the API:
``` curl -X GET 'http://localhost:5004/api/statistics?start_date=2023-04-14&end_date=2023-04-14&symbol=IBM' ```

**The sample response will look like:**

```
{
    "data": {
        "average_daily_close_price": 128.14,
        "average_daily_open_price": 128.46,
        "average_daily_volume": 4180614.0,
        "end_date": "2023-04-14",
        "start_date": "2023-04-14",
        "symbol": "IBM"
    },
    "info": {
        "error": ""
    }
}
```

# Secret Key storage explanation

**Local** :In the local development environment, the API key is set up as an environment variable in the docker-compose.yml file. This approach ensures that the key is easily accessible during development while keeping it separate from the application code.<br />
**Production** : In production, I will utilize AWS Secrets Manager to securely store and manage our API keys. This ensures that sensitive information is protected and can be easily rotated or updated as needed.

