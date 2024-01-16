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
