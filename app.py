from flask import Flask, request, jsonify, url_for
from functools import wraps
import traceback
import requests

app = Flask(__name__)

# Dummy user credentials
USER_CREDENTIALS = {
    "username": "your_username",
    "password": "your_password"
}


def error_handler(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify(
                {
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "error_traceback": str(traceback.format_exc()) if type(e).__name__ != "SystemError" else None
                }
            )

    return wrapper


# Authentication decorator
def authenticate(f):
    @wraps(f)
    @error_handler
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            raise NotImplementedError("Missing API Token, this API call is protected and expects the API token in "
                                      "the additional header 'Authorization'. You can generate API token through "
                                      "'/auth?username=your_username&password=your_password'. Please refer to the "
                                      "documentation.")
        if auth_token != f"{USER_CREDENTIALS['username']}:{USER_CREDENTIALS['password']}":
            raise PermissionError('Authentication failed, Invalid API Token')

        return f(*args, **kwargs)

    return decorated_function


# API endpoint to generate auth token
@app.route('/auth', methods=['POST'])
@error_handler
def generate_auth_token():
    data = request.get_json()
    if data and data.get('username') == USER_CREDENTIALS['username'] and data.get('password') == USER_CREDENTIALS[
        'password']:
        return jsonify({'token': f"{USER_CREDENTIALS['username']}:{USER_CREDENTIALS['password']}"})
    elif (data and ('username' not in data or 'password' not in data)) or not data:
        raise NotImplementedError("Invalid API call, '/auth' API call expects .JSON file with 'username' and "
                                  "'password' keys")
    raise PermissionError("Invalid credentials, either 'username' or 'password' or both are incorrect")


# Protected API endpoint to fetch detailed information about a specific country
@app.route('/country', methods=['GET'])
@authenticate
@error_handler
def get_country_info():
    name = request.args.get('name')
    if not name:
        raise NotImplementedError(
            "Required Parameter Missing, this API call expects 'name' with full name of country ")

    # RESTCountriesAPI API call
    try:
        response = requests.get(url=f"https://restcountries.com/v3.1/name/{name}?fullText=true")
        response = response.json()
    except:
        raise SystemError("Internal API Error")

    return jsonify({'result': response})


# Protected API endpoint to retrieve a list of countries based on filters and sorting
@app.route('/countries_list', methods=['GET'])
@authenticate
@error_handler
def get_countries_list():
    page = int(request.args.get('page', 1))
    items_per_page = int(request.args.get('items_per_page', 10))  # Default items per page is 10
    sort_by = request.args.get('sort_by')  # Default sort by population
    sort_order = request.args.get('sort_order', 'asc')  # Default sort order is ascending

    # Implement logic to fetch and filter countries from the RESTCountriesAPI
    # Handle errors and return the response as JSON
    if sort_by and sort_by not in ('area', 'population'):
        raise NameError(
            f"please note that 'sort_by' parameter only takes either of 'area' and 'population', got '{sort_by}'")
    elif sort_by and sort_order not in ("asc", 'desc'):
        raise NameError(f"'sort_order' should be either 'asc' or 'desc', got '{sort_order}'")

    # RESTCountriesAPI API call
    try:
        response = requests.get(url="https://restcountries.com/v3.1/all?fields=name,population,area,languages")
        response = response.json()
    except:
        raise SystemError("Internal API Error")

    # Filter by population
    min_population = int(request.args.get('min_population', 0))
    max_population = float(request.args.get('max_population', float('inf')))
    response = [country for country in response
                if min_population <= country.get('population', 0) <= max_population]

    # Filter by area
    min_area = float(request.args.get('min_area', 0))
    max_area = float(request.args.get('max_area', float('inf')))
    response = [country for country in response
                if min_area <= country.get('area', 0) <= max_area]

    # Filter by language
    target_language = request.args.get('languages')
    if target_language:
        response = [country for country in response
                    if any(lang.lower() in target_language.lower().split(",") for lang in
                           country.get('languages', {}).values())]

    # Sorting
    if sort_by:
        reverse_order = sort_order.lower() == 'desc'
        response.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse_order)

    # Pagination Implementation
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paginated_countries = response[start_index:end_index]

    # Calculate total number of pages
    total_items = len(response)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    # Preserve existing query parameters
    existing_params = request.args.copy()
    if 'page' in existing_params:
        del existing_params['page']

    # Generate URLs for next_page and previous_page
    next_page_url = url_for('get_countries_list', page=page + 1, **existing_params) if page < total_pages else None
    previous_page_url = url_for('get_countries_list', page=page - 1, **existing_params) if page > 1 else None

    # Return the paginated and filtered result as JSON
    return jsonify(
        {
            "total": len(paginated_countries),
            "page_size": items_per_page,
            "page": page,
            "prev_page": previous_page_url,
            "next_page": next_page_url,
            "result": list(map(lambda x: x.get('name'), paginated_countries))
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
