#Python program to find the years between 2000 and 2150 when the 25th of December is a Sunday.

from itertools import product
from datetime import datetime

start_year = 2000
end_year = 2150


years_and_days = product(range(start_year, end_year + 1), [25, 12])  


sundays = [(year, day) for year, day in years_and_days if datetime(year, 12, day).weekday() == 6]


for year, day in sundays:
    print(f"The 25th of December in {year} is a Sunday.")
