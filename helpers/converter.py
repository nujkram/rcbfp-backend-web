import os
import csv
from csv import DictReader

work_path = os.path.dirname(os.path.abspath(__file__))


def import_data():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv')) as file:
        reader = csv.reader(file)
        data = list(reader)
        return data


def import_addresses():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv')) as file:
        addresses = [row['address'] for row in DictReader(file)]

        return addresses


def import_businesses():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv')) as file:
        businesses = [row['name'] for row in DictReader(file)]

        return businesses


def import_building_data():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv'), mode='r') as file:
        reader = csv.reader(file)
        data = {}
        for rows in reader:
            name, address, building = rows
            data[building] = address

    return data


def import_business_data():
    with open(os.path.join(work_path, 'fixtures/roxas_businesses.csv'), mode='r') as file:
        reader = csv.reader(file)
        data = {}
        for rows in reader:
            name, address, building = rows
            data[name] = address

    return data
