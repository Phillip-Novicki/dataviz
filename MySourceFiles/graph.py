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

def visualize_type():
    """Visualize data by category in a bar graph"""

    #grab our parsed data
    data_file = parse(MY_FILE, ",")
    
    #Same as before, this returns a dict where it sums the total
    # incidents per Category
    counter = Counter(item["Category"] for item in data_file)

    #Set the labels which are based on the keys of our counter.
    #Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())

    xlocations = np.arange(len(labels)) + 0.5

    #width of each bar
    width = 0.5

    #Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    #Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)
    
    #Make the overal graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    #Save the clocktower, err.. plot!
    plt.savefig("Type.png")

    #Close figure
    plt.clf()

def main(): 
    visualize_type()

if __name__ == "__main__":
    main()