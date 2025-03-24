# Day 7: Weather Oracle - Visualizing Temperature Trends

## Objective
The goal of this project is to visualize temperature trends using weather data. This helps to track climate change and understand how the world's climate has shifted over time.

## Project Overview
You work for a cutting-edge environmental organization tracking climate change data. Your mission is to visualize temperature trends over time using various data visualization techniques.

## Files
- **weather_oracle_visualizing_temperature_trends.py**
  - This Python script contains the code to load, process, and visualize the temperature data.
- **Weather Oracle: Visualizing Temperature Trends.ipynb - Colab.pdf**
  - This PDF contains the notebook used in Google Colab for the project.

## Data Source
The data used in this project is from the Global Land Temperatures By City dataset. 

## Code Explanation
### Loading Data
The dataset is loaded using pandas:
```python
import pandas as pd

# Load dataset
df = pd.read_csv("/content/GlobalLandTemperaturesByCity.csv")
