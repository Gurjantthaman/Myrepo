import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap API endpoint and your API key
API_KEY = "2b6ca8a7ac342cfbfd622209e101eba2"  # Replace with your actual OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


# Function to get weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()  # Get the city entered by the user
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Construct the full URL for the API request
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    try:
        # Make the API request
        response = requests.get(url)
        data = response.json()

        # Print the response data to check the structure (for debugging)
        print(data)

        # Check if the API response was successful
        if data.get("cod") != 200:  # If "cod" is not 200, there was an error
            error_message = data.get("message", "Unknown error")
            messagebox.showerror("Error", f"Failed to get weather: {error_message}")
            return

        # Extract weather information
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]

        # Update the GUI with the weather information
        result_label.config(
            text=f"Weather: {description.capitalize()}\n"
                 f"Temperature: {temperature}°C\n"
                 f"Pressure: {pressure} hPa\n"
                 f"Humidity: {humidity}%"
        )

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Could not retrieve weather data. Please try again later.")
        print(e)


# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  # Size of the window

# Add a label for the title
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 20), pady=10)
title_label.pack()

# Add an entry widget for the city name
city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12))
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)

# Add a button to get weather information
get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather)
get_weather_button.pack(pady=10)

# Add a label to display the weather information
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

