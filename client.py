import random
import requests
import threading
import os
from dotenv import load_dotenv
import time

# Работа с переменными окружения
load_dotenv()
thred_quantity = int(os.getenv("thread_quantity"))
request_delay = int(os.getenv("request_delay"))

# """В задании буквально написано, что строка выглядит следующим образом: '{208.33.245.18} {PUT} {http://my-example.com} {108}' """


responses = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


def log(data: str) -> None:

    data = data + "\n"

    with open('logged_data.log', 'a', encoding='utf-8') as f:
        f.write(data)


def generate_request_data() -> str:

    address = '.'.join([str(random.randint(1, 256)) if i == 0 else str(random.randint(0, 256)) for i in range(4)])
    method = random.choice(responses)
    # Сделать генерацию рандомного адреса?
    uri = 'http://my-example.com'
    status_code = random.randint(100, 600)

    request_data = f"{{{address}}} {{{method}}} {{{uri}}} {{{status_code}}}"


    return request_data


def send_post_request(data: generate_request_data) -> None:

    try:
        request_data = {"log": data}
        response = requests.post("http://127.0.0.1:8000/api/data", json=request_data)
        # Данные логируются только в случае успеха отправки данных
        log(data)
        # Для проверки работы в консоли
        print(response.status_code) 

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


while True:
    for i in range(thred_quantity):

        thread = threading.Thread(target=send_post_request, args=(generate_request_data(), ), daemon=True)
        thread.start()
        thread.join()

    time.sleep(random.uniform(0, request_delay / 1000.0))
