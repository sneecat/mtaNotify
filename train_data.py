#!/usr/bin/env python
import csv
import requests
from protobuf_to_dict import protobuf_to_dict
from google.transit import gtfs_realtime_pb2
from trainurls import urldict
from mta_routes import train_list, route_list, list_my_stations

class mtagtfs():
    trip_updates = {}
    vehicle_updates = {}
    arrival_times = []

    def __init__(self, train, station=None, route=None):
        if station is None:
            print(
            '''
            use list_stations() to see a list
            of stations associated with your
            selected train.
            '''
                    )
        if train not in train_list:
            print('please enter a valid train line ex. mtagtfs(\'G\')')
        else:
            self.station = station
            self.train = train.upper()
            self.route = route

    def list_stations(self):
        if self.train not in train_list:
            print('please enter a valid train with set_train()')
        else:
            list_my_stations(self.train)
        # DONE offload this to mta_routes.py

    def list_trains(self):
        # offloaded this work to mta_routes.py
            print(train_list)

    def set_api(self, api_input):
        self.api_key = api_input
    def set_train(self, new_train_letter):
        """Sets the route based on the single letter train ID
        """ 
        if new_train_letter in train_list:
            self.train = new_train_letter.upper()
            print(f'train set to {self.train}')
    def update(self):
        """
        gets raw data from MTA GTFS-rt API 

        data is updated ~once/min, so no need to call more often than that. must be called before querying arrival times.
        """
        if len(self.api_key) < 40 or len(self.api_key) > 40:
            print("invalid API key")
            return
        feed = gtfs_realtime_pb2.FeedMessage()
        # gets proper URL based on chosen train route
        for route_url in urldict:
            if self.train in route_url:
                mta_url = urldict[route_url]
        response = requests.get(mta_url, headers={'x-api-key' : (self.api_key)})
        feed.ParseFromString(response.content)
        mta_raw_output = protobuf_to_dict(feed)
        print(mta_raw_output)
        for key in mta_raw_output:
            if key is 'vehicle':
                
        self.vehicle_updates = {val for key, val in mta_raw_output.items() if 'vehicle' in key} 
        self.trip_updates = {val for key, val in mta_raw_output.items() if 'trip_update' in key}
        print(self.trip_updates)
        print(self.vehicle_updates)
# TODO split dictionary by vehicle and trip updates
    def arrival_time(self, direction):
        trip_updates = {}


