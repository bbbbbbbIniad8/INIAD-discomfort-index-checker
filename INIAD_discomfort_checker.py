import requests
from requests.auth import HTTPBasicAuth


def get_info(id, password, room):
    url = f"https://edu-iot.iniad.org/api/v1/sensors/{room}"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(id, password))
        response_data = response.json()
        return response_data

    except Exception as e:
        print({"status": "error", "description": str(e)})


def discomfort_index(temperature, humidity):
    return 0.81 * temperature + 0.01 * humidity * (0.99 * temperature - 14.3) + 46.3


def display_result(data):
    try:
        room_num = data[1]['room_num']
        humidity_entry = data[1]
        temperature_entry = data[-1]

        temperature = temperature_entry["value"]
        humidity = humidity_entry["value"]
        result = discomfort_index(temperature, humidity)
        print(f"教室[{room_num}]-------------------------------")
        print(f"温度: {temperature}")
        print(f"湿度: {humidity}")
        print(f"不快度指数:{result}\n")

    except KeyError as e:
        if data['status'] == 'error' and data['description'] == 'Service available only on INIAD LAN':
            print("外部ネットワークではサービスを利用することはできません。")
        elif data['status'] == 'error' and data['description'] == 'Sensors not accessible':
            print("この教室のセンサーにはアクセスできません。")
        elif data['status'] == 'error' and data['description'] == "'username' or 'password' is invalid":
            print("与えられたユーザーネーム、もしくはパスワードに誤りがあります。")

