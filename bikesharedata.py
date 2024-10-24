# Rewriting the Python code to generate a downloadable Python script after the execution state reset.

import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Define station information for Hyderabad
stations = [
    {'Station_ID': 'ST001', 'Station_Location': 'Banjara Hills'},
    {'Station_ID': 'ST002', 'Station_Location': 'Gachibowli'},
    {'Station_ID': 'ST003', 'Station_Location': 'Jubilee Hills'},
    {'Station_ID': 'ST004', 'Station_Location': 'Madhapur'},
    {'Station_ID': 'ST005', 'Station_Location': 'Begumpet'},
    {'Station_ID': 'ST006', 'Station_Location': 'Hitech City'},
    {'Station_ID': 'ST007', 'Station_Location': 'Kondapur'},
    {'Station_ID': 'ST008', 'Station_Location': 'Shamshabad'},
    {'Station_ID': 'ST009', 'Station_Location': 'Kukatpally'},
    {'Station_ID': 'ST010', 'Station_Location': 'Secunderabad'}
]

# Define seasons and weather conditions
seasons = {
    'Summer': ('March', 'April', 'May'),
    'Monsoon': ('June', 'July', 'August', 'September'),
    'Post-Monsoon': ('October', 'November'),
    'Winter': ('December', 'January', 'February')
}
weather_conditions = {
    'Summer': ['Sunny', 'Hot'],
    'Monsoon': ['Rainy', 'Cloudy'],
    'Post-Monsoon': ['Clear', 'Partly Cloudy'],
    'Winter': ['Cold', 'Clear']
}

# Function to generate random trips for each day
def generate_trip_data(start_date, end_date):
    data = []
    current_date = start_date
    user_id_counter = 1

    while current_date <= end_date:
        year = current_date.year
        month = current_date.strftime('%B')
        day_of_week = current_date.strftime('%A')
        holiday = random.choice(['Yes', 'No']) if day_of_week in ['Saturday', 'Sunday'] else 'No'
        working_day = 'No' if holiday == 'Yes' else 'Yes'

        # Determine season and weather based on month
        season = next((s for s, months in seasons.items() if month in months), 'Unknown')
        weather = random.choice(weather_conditions[season])

        # Generate trips for each hour of the day (8 AM to 8 PM)
        for hour in range(8, 21):
            station = random.choice(stations)
            user_age = random.randint(18, 65)
            user_gender = random.choice(['Male', 'Female'])
            trip_duration = random.randint(10, 60)  # Duration in minutes
            temperature = random.uniform(20, 40) if season != 'Winter' else random.uniform(15, 25)
            rider_type = random.choice(['Casual', 'Subscriber'])
            bike_type = random.choice(['Standard Bike', 'Electric Bike', 'Premium Bike'])

            trip_data = {
                'Date': current_date.strftime('%Y-%m-%d'),
                'Time': f'{hour:02d}:00',
                'Year': year,
                'Month': month,
                'Hour': hour,
                'Holiday': holiday,
                'Working Day': working_day,
                'Weekday': day_of_week,
                'Temperature': round(temperature, 1),
                'Station ID': station['Station_ID'],
                'Station Location': station['Station_Location'],
                'User ID': f'U{user_id_counter:04d}',
                'User Age': user_age,
                'User Gender': user_gender,
                'Trip Duration': trip_duration,
                'Trip Start Time': f'{hour:02d}:00',
                'Trip End Time': f'{(hour + trip_duration // 60) % 24:02d}:{trip_duration % 60:02d}',
                'Season': season,
                'Weather Conditions': weather,
                'Rider Type': rider_type,
                'Bike Type': bike_type
            }
            data.append(trip_data)
            user_id_counter += 1

        current_date += timedelta(days=1)

    return pd.DataFrame(data)

# Generate data for years 2022, 2023, and up to October 25, 2024
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 10, 25)
dataset = generate_trip_data(start_date, end_date)

# Display the first few rows of the dataset
print(dataset.head())

# Save dataset to CSV
dataset.to_csv('hyderabad_bike_share_data.csv', index=False)