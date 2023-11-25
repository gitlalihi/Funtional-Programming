#Python program that implements a Python program that filters out dates (in the format "YYYY-MM-DD") that are in the future using the filter function.
from datetime import datetime

def is_date_in_future(date_str):
    
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    
    
    current_date = datetime.now().date()
    
    
    return date_object.date() > current_date

def main():
    
    date_list = ["2022-01-01", "2023-11-25", "2023-01-01", "2022-12-31", "2024-01-01"]
    
    
    filtered_dates = list(filter(is_date_in_future, date_list))
    
    
    print("Filtered Dates:", filtered_dates)

if __name__ == "__main__":
    main()
