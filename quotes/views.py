
import json
from django.shortcuts import render
from pathlib import Path
from datetime import datetime

def Home(request):
    # Path to your JSON file within the static directory
    json_file_path = Path('C:/Users/vinee/OneDrive/Desktop/Random-Quotes/random_quotes/quotes/static/data.json')
    
    # Load JSON data from file with UTF-8 encoding
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Calculate the day of the year (1-365)
    day_of_year = datetime.now().timetuple().tm_yday
    
    # Ensure we don't go out of bounds if data has fewer than 365 quotes
    quote_index = day_of_year % len(data)
    
    # Get the quote of the day
    quote_of_the_day = data[quote_index]
    
    # Pass the quote to the template
    return render(request, 'home.html', {'quote': quote_of_the_day})
