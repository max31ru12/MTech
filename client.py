import random
import requests
import json
import logging

# """В задании буквально написано, что строка выглядит следующим образом: '{208.33.245.18} {PUT} {http://my-example.com} {108}' """


responses = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


def log(data: str) -> None:

    data = data + "\n"

    with open('logged_data.log', 'a', encoding='utf-8') as f:
        f.write(data)


def generate_request_data() -> str:

    address = '.'.join([str(random.randint(1, 256)) if i == 0 else str(random.randint(0, 256)) for i in range(4)])
    method = random.choice(responses)
    uri = 'http://my-example.com'
    status_code = random.randint(100, 600)

    request_data = f"{{{address}}} {{{method}}} {{{uri}}} {{{status_code}}}"


    return request_data


def send_post_request(data: generate_request_data) -> None:

    try:
        request_data = {"log": data}
        response = requests.post("http://127.0.0.1:8000/api/data", json=request_data)
        # Может быть логировать надо в другом месте???
        log(request_data)
        print(response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


generate_request_data()








