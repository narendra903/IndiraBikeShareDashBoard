# Writing the Python code for Table 2 provided above to a .py file for download

import pandas as pd
import random

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

# Define years for which data is needed
years = [2022, 2023, 2024]

# Generate Financial Information
def generate_financial_data(stations, years):
    data = []

    for station in stations:
        for year in years:
            cogs = random.randint(10, 30)  # Cost of Goods Sold
            price_per_minute = round(random.uniform(2.0, 4.0), 2)  # Price per minute

            financial_data = {
                'Station ID': station['Station_ID'],
                'Station Location': station['Station_Location'],
                'Year': year,
                'COGS': cogs,
                'Price per Minute': price_per_minute
            }
            data.append(financial_data)

    return pd.DataFrame(data)

# Generate the financial dataset
financial_dataset = generate_financial_data(stations, years)

# Display the first few rows of the dataset
print(financial_dataset.head())

# Save dataset to CSV
financial_dataset.to_csv('hyderabad_bike_share_financial_data.csv', index=False)
