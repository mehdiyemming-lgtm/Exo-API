import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 45.46,
        "longitude": -73.47,
        "current": "temperature_2m",
    },
    headers={"Accept": "application/json"},
    timeout=10,
)

# print(response.status_code)
# print(response.url)

la=response.json()


t =la["current"]["temperature_2m"]
u = la["current_units"]["temperature_2m"]

print(f"La température est de {t} {u}")