import requests

API_KEY = "77b45698b945bc7944af37ccac71928f"


def get_data(place, forecasted_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecasted_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place="Tokyo", forecasted_days=3, kind="Sky"))
