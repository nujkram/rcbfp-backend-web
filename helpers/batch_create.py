from autofixture import AutoFixture
import random

from buildings.models.building.building_models import Building
from business.models import Business
from checklists.models.checklist.checklist_models import Checklist
from datesdim.models import DateDim
from incidents.models.incident.incident_models import Incident
from locations.models import Region, Province, City

region = Region.objects.get(pk=6)
province = Province.objects.get(pk=22)
city = City.objects.get(pk=381)


def businesses(data):
    for key, item in data.items():
        __building = item['building']
        __business = item['business']
        __address = item['address']
        __latitude = item['latitude']
        __longitude = item['longitude']

        building = Building.objects.filter(name=__building)
        business = Business.objects.filter(name=__business)
        if building:
            if business:
                continue
            fixture = AutoFixture(
                Business,
                field_values={
                    'name': __business,
                    'address': __address,
                    'region': region,
                    'province': province,
                    'city': city,
                    'building': building[0]
                }
            )

            fixture.create(1)
        else:
            fixture = AutoFixture(
                Building,
                field_values={
                    'name': __building,
                    'address': __address,
                    'region': region,
                    'province': province,
                    'city': city,
                    'latitude': __latitude,
                    'longitude': __longitude
                }
            )

            fixture.create(1)
            building = Building.objects.last()

            business = AutoFixture(
                Business,
                field_values={
                    'name': __business,
                    'address': __address,
                    'region': region,
                    'province': province,
                    'city': city,
                    'building': building
                }
            )

            business.create(1)


def buildings(buildings):
    for building in buildings:
        fixture = AutoFixture(
            Building,
            field_values={
                'name': building,
                'address': buildings[building]['address'],
                'region': region,
                'province': province,
                'city': city,
                'latitude': buildings[building]['latitude'],
                'longitude': buildings[building]['longitude']
            }
        )

        fixture.create(1)

    return print('Buildings created')


def checklists(businesses, year):
    schedule = DateDim.objects.get_days_between(start=f'{year}-01-01', end=f'{year}-12-31')

    for business in businesses:
        fixture = AutoFixture(
            Checklist,
            field_values={
                'business': business,
                'building': business.building,
                'date_checked': random.choice(schedule)
            }
        )

        fixture.create(1)

    return print('Checklists created')


def incidents(incident_count, year):
    date_choices = DateDim.objects.get_days_between(start=f'{year}-01-01', end=f'{year}-12-31')
    business = Business.objects.all()

    for i in range(0, incident_count):
        victim = random.choice(business)
        fixture = AutoFixture(
            Incident,
            field_values={
                'business': victim,
                'building': victim.building,
                'incident_type': 'Structural',
                'occurrence': random.choice(date_choices),
                'region': region,
                'province': province,
                'city': city
            }
        )

        fixture.create(1)

    return print('Dummy incident created')
