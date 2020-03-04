import os
import csv
from csv import DictReader

work_path = os.path.dirname(os.path.abspath(__file__))


def import_building_data():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv'), mode='r') as file:
        reader = csv.reader(file)
        data = {}
        next(reader)
        for rows in reader:
            name, address, building, latitude, longitude = rows
            data[building] = {
                'business': name,
                'building': building,
                'address': address,
                'latitude': latitude,
                'longitude': longitude,
            }

    return data
