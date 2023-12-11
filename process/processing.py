import requests
import time
import threading



def get_request() -> None:

    try:

        response = requests.get("http://127.0.0.1:8000/api/data")
        print(response.status_code)
        data = response.text + "\n"
        
        with open("mounted.txt", "a") as file:
            file.write(data)
    
    except Exception as e:
        print(f"Произошла ошибка при получении данных: {e}")


while True:
    thread = threading.Thread(target=get_request, args=())
    thread.daemon = True
    thread.start()
    thread.join()
    # Периодечское выполнение
    time.sleep(20)

