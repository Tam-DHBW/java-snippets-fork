import random

def generate_weather(city):
    temperatures = list(range(-10, 35))  # Temperature range from -10 to 35 degrees
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Thunderstorm", "Foggy"]

    temperature = random.choice(temperatures)
    condition = random.choice(conditions)

    return f"Weather in {city}: {condition}, {temperature}°C"

if __name__ == "__main__":
    city = input("Enter your city: ")
    forecast = generate_weather(city)
    print(forecast)
