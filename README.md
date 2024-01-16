# Country API Service

Welcome to the Country API service! This backend service provides information about countries, including details about specific countries and a list of countries based on various filters. The service is built using Python and Flask.

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
4. [Error Handling](#error-handling)
5. [Run the Service](#run-the-service)
6. [Testing with cURL](#testing-with-curl)


## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/countryinfo-api.git
cd country-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Authentication

### Generate API Token
To access protected endpoints, you need to generate an API token. Now for demonstration purposes and to avoid using a database as of now use username = 'your_username' and password = 'your_password'. Use the following endpoint:

#### Endpoint: `/auth`
#### Method: POST

#### Request:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

#### Response:
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

### `/countries` Endpoint
    Method: GET
    Retrieve a list of countries based on filters and sorting criteria.

#### Filters, Sorting and pagination
#### Sorting:
    sort_by: Sort by either 'area' or 'population'.
    sort_order: Sort order, either 'asc' or 'desc'.
    
#### Filters:
    min_population, max_population: Filter countries by population range.
    min_area, max_area: Filter countries by area range.
    languages: Filter countries by language.
    
#### Pagination:
    page: Page number.
    items_per_page: Number of items per page.
    
## Error Handling
In case of errors, the API provides detailed error messages, including the type and traceback.

## Run the Service
Run the Flask application:

```bash
python app.py
```

## Testing with cURL
Here are some cURL commands to test the API endpoints:

### Generate API Token:
Please note that to avoid using a database as of now, username and password are included in the code itself. Use username = "your_username" and password = "your_password" as it is.

```bash
curl -X POST "http://localhost:5000/auth" -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}'
```

### Fetch Country Information:
```bash
curl -X GET "http://localhost:5000/country/name?name=CountryName" -H "Authorization: your_generated_token"
```

### Retrieve List of Countries:
```bash
curl -X GET "http://localhost:5000/countries?page=1&items_per_page=10" -H "Authorization: your_generated_token"
```

Feel free to modify the parameters based on your testing needs.
