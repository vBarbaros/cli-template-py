import requests
from requests.exceptions import ConnectionError


def get_generic(path_var):
    # Make a GET request to the API endpoint
    try:
        response = requests.get('https://api.example.com/endpoint' + path_var)
        # Check the status code of the response
        if response.status_code == 200:
            # Print the JSON data returned by the API
            print(response.json())
        else:
            # Print the status code if the request was not successful
            print('Error:', response.status_code)
    except ConnectionError:
        print('Connection Error: Please provide a valid URL')


def post_generic(path_var):
    try:
        url = 'http://example.com/api/v1/create/' + path_var
        data = {'name': 'John Smith', 'email': 'john@example.com'}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print('Success:', response.json())
        else:
            print('Error:', response.status_code)
    except ConnectionError:
        print('Connection Error: Please provide a valid URL')


def put_generic(path_var):
    try:
        url = 'http://example.com/api/v1/update/' + path_var
        data = {'name': 'John Smith', 'email': 'john@example.com'}
        response = requests.put(url, json=data)
        if response.status_code == 200:
            print('Success:', response.json())
        else:
            print('Error:', response.status_code)
    except ConnectionError:
        print('Connection Error: Please provide a valid URL')


def delete_generic(path_var):
    try:
        url = 'http://example.com/api/v1/delete/' + path_var
        response = requests.delete(url)
        if response.status_code == 200:
            print('Success:', response.json())
        else:
            print('Error:', response.status_code)
    except ConnectionError:
        print('Connection Error: Please provide a valid URL')
