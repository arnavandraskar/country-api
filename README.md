# CountryInfo API Service

Welcome to the CountryInfo API service! This backend service provides information about countries, including details about specific countries and a list of countries based on various filters. The service is built using Python and Flask.

## Table of Contents

1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Authentication](#authentication)
    - [Generate API Token](#generate-api-token)
    - [Include API Token](#include-api-token)
3. [Endpoints](#endpoints)
    - [`/auth`](#auth-endpoint)
    - [`/country/name`](#countryname-endpoint)
    - [`/countries`](#countries-endpoint)
4. [Filters and Sorting](#filters-and-sorting)
5. [Pagination](#pagination)
6. [Error Handling](#error-handling)
7. [Run the Service](#run-the-service)
    - [Using Docker](#using-docker)
8. [Testing with cURL](#testing-with-curl)


## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/countryinfo-api.git
cd countryinfo-api

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Authentication

### Generate API Token
To access protected endpoints, you need to generate an API token. Use the following endpoint:

#### Endpoint: /auth
#### Method: POST

#### Request:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

####Response:
```json
{
    "token": "your_generated_token"
}
```

### Include API Token
Include the generated API token in the Authorization parameter when making requests to protected endpoints.

```bash
curl -X GET "http://localhost:5000/country/name?name=CountryName" -H "Authorization: your_generated_token"
```

## Endpoints

### `/auth` Endpoint
    Method: POST
    Generate an API token by providing valid credentials. It expects .json in url body which has username and password values as mentioned in the Authenticate section.

### `/country/name` Endpoint
Method: GET

Fetch detailed information about a specific country by providing its name.

/countries Endpoint
Method: GET

Retrieve a list of countries based on filters and sorting criteria.

Filters and Sorting
Sorting:

sort_by: Sort by either 'area' or 'population'.
sort_order: Sort order, either 'asc' or 'desc'.
Filters:

min_population, max_population: Filter countries by population range.
min_area, max_area: Filter countries by area range.
languages: Filter countries by language.
Pagination
page: Page number.
items_per_page: Number of items per page.
Error Handling
In case of errors, the API provides detailed error messages, including the type and traceback.

Run the Service
Run the Flask application:

bash
Copy code
python app.py
Using Docker
Alternatively, you can use Docker to run the service:

bash
Copy code
docker build -t countryinfo-api .
docker run -p 5000:5000 countryinfo-api
Visit http://localhost:5000 in your browser or use a tool like curl or Postman to interact with the API.

Testing with cURL
Here are some cURL commands to test the API endpoints:

Generate API Token:
bash
Copy code
curl -X POST "http://localhost:5000/auth" -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}'
Fetch Country Information:
bash
Copy code
curl -X GET "http://localhost:5000/country/name?name=CountryName" -H "Authorization: your_generated_token"
Retrieve List of Countries:
bash
Copy code
curl -X GET "http://localhost:5000/countries?page=1&items_per_page=10" -H "Authorization: your_generated_token"
Feel free to modify the parameters based on your testing needs.
