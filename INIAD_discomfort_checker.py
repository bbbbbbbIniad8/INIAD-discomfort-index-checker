import requests
import requests
from requests.auth import HTTPBasicAuth

class DiscomfortIndexInINIAD:
    @classmethod
    def get_info(cls, id, password, room):
        url = f"https://edu-iot.iniad.org/api/v1/sensors/{room}"
        try:
            response = requests.get(url, auth=HTTPBasicAuth(id, password))
            response_data = response.json()
            return response_data

        except Exception as e:
            print({"status": "error", "description": str(e)})

    @classmethod
    def discomfort_index(cls, temperature, humidity):
        return 0.81 * temperature + 0.01 * humidity * (0.99 * temperature - 14.3) + 46.3

    @classmethod
    def display_result(cls, data):
        room = data[1]['room_num']
        temperature = data[-1]["value"]
        humidity = data[1]["value"]
        result = cls.discomfort_index(temperature, humidity)
        print(f"教室[{room}]-------------------------------")
        print(f"温度: {temperature}")
        print(f"湿度: {humidity}")
        print(f"不快度指数:{result}\n")
