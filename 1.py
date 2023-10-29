import csv 
# Here we are opening the CSV file in read mode only 
with open('weather_data.csv', mode="r") as file: 
    # Here we are creating a CSV reader that will read the content
    csv_reader = csv.reader(file)
    # Here we are trying to process internal data 
    for row in csv_reader: 
        print(row[0])