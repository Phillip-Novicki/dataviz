import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


MY_FILE="../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""
    
    # Open CSV file
    opened_file = open(raw_file)

    # Read the CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    # Setup an empty list
    parsed_data = []
    
    # Skip over the first line of the file for the headers
    fields = next(csv_data)

    # Iterate over each row of the csv file, zip together fields >>
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file

    opened_file.close()

    return parsed_data

def visualize_days():
    """Visualize data by day of week"""

    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen each day of week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data (the days of the week) from the 
    # 'counter' variable from the y-axis data (the number of incidents
    # for each day)
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)
# create the amount of ticks needed for our x-axis and assign
# the labels

    # save the plot!
    plt.savefig("Days.png")

    #close plot file
    plt.clf()

def main():
    visualize_days()

if __name__ == "__main__":
    main()