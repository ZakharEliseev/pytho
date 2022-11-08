WEATHER_FORCAST = {
    'moscow': {
        'temp': 13,
        'humidity': 40,
        "rain chance": 52,
    },
    'voronezh': {
        "rain chance": 50,
    }
}


def get_weather_condition(city: str):
    city = city.lower()  # вариант 2
    # if city not in WEATHER_FORCAST:
    # #if (forecast := WEATHER_FORCAST.get(city.lower())) is not None: # вариант 1
    #    return ValueError("Invalid city")
    # return WEATHER_FORCAST[city]
    forecast = WEATHER_FORCAST.get(city)  # вариант 3
    if forecast is None:
        raise ValueError(f"Invalid city {city!r}")
    return forecast


def rain_tomorrow(city: str) -> bool | None:
    print('Will it rain', city)
    try:
        weather = get_weather_condition(city)
    except (ValueError, TypeError):
        return None
    return weather["rain chance"] > 50


# print(get_weather_condition('Moscow'))
# print(get_weather_condition('sochi'))
# print(get_weather_condition('Voronezh'))
print(rain_tomorrow('Moscow'))
print(rain_tomorrow('Sochi'))
print(rain_tomorrow('Voronezh'))
