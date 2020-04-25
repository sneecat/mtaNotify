#!/usr/bin/env python
import csv
route_list = {
        'ACE': ['A', 'C', 'E'],
        'BDFM': ['B', 'D', 'F', 'M'],
        'G': ['G'],
        'L': ['L'],
        'JZ': ['J', 'Z']
        }


# a flattened list of trains to check against
train_list = [item for sublist in route_list.values() for item in sublist]


def list_my_stations(my_train):
    with open('mta_stations_info.csv', newline='') as csvfile:
        station_dict = csv.DictReader(csvfile)
        for row in station_dict:
            if my_train in row['Daytime Routes']:
                print(row['Stop Name'], row['GTFS Stop ID'])
#            print(
#                row['GTFS Stop ID'],
#                row['Stop Name'],
#                row['Daytime Routes'],
#                row['GTFS Latitude'],
#                row['GTFS Longitude'],
#                row['North Direction Label'],
#                row['South Direction Label']
#                )
