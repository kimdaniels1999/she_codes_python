import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"  # no change required

    """Takes a temperature and returns it in string format with the degrees and celcius symbols..

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    pass

def convert_date(iso_string):
    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z") #added variable 
    date_new = date.strftime("%A %d %B %Y") # use previous variable, datetime changed to date, forgot to add "" inside parenthesis,  
    return date_new   # return 2nd new variable
    """Converts an ISO formatted date into a human readable format.

    Args
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit):  # (temp_in_farenheit is an int)
    return round((float(temp_in_farenheit)-32)*(5/9),1) # round(number, 1) #combine all to one line 

    """Converts a temperature from farenheit to celcius. 

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp. 
    """
    pass

mean = []
def calculate_mean(weather_data): # what format is the weather data (error = unsupported operand types +: 'int' and 'str')
    for numbers in weather_data:
        numbers = numbers +=
        
    calculate_mean = sum(data) / len(data)
    return float(calculate_mean)
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


def load_data_from_csv(csv_file):

    data_list = []  # create an empty list
    with open(csv_file, mode="r", encoding="utf-8") as csv_file:  #open csv file
        csv_reader = csv.reader(csv_file, delimiter = ",")  #read csv file
        for index, row in enumerate(csv_reader):   #two loop variables index and row
            if index != 0 and len(row) != 0:   # index is not equal to zero lenth of row is not equal to zero (non-empty lines)
                data_list.append([row[0],int(row[1]),int(row[2])])  #append to the empty list 
    return data_list

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

def find_min(weather_data):
    
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    if len(weather_data) == 0:
        return()
    for i in range(0, len(weather_data)):
        maxi = round(float)

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass