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


def businesses(businesses):
    for business in businesses:
        try:
            building = Building.objects.get(name=business[2])

            fixture = AutoFixture(
                Business,
                field_values={
                    'name': business[0],
                    'address': business[1],
                    'building': building,
                    'region': region,
                    'province': province,
                    'city': city
                }
            )

            fixture.create(1)
        except Building.DoesNotExist:
            building = AutoFixture(
                Building,
                field_values={
                    'name': business[2],
                    'address': business[1],
                    'region': region,
                    'province': province,
                    'city': city
                }
            )

            building.create(1)

            building = Building.objects.get(name=business[2])
            fixture = AutoFixture(
                Business,
                field_values={
                    'name': business[0],
                    'address': business[1],
                    'building': building,
                    'region': region,
                    'province': province,
                    'city': city
                }
            )

            fixture.create(1)

    return print('Businesses created')


def buildings(buildings):
    for building in buildings:
        fixture = AutoFixture(
            Building,
            field_values={
                'name': building,
                'address': buildings[building],
                'region': region,
                'province': province,
                'city': city
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


def incidents(count, year):
    date_choices = DateDim.objects.get_days_between(start=f'{year}-01-01', end=f'{year}-12-31')
    business = Business.objects.all()

    for i in range(0, count):
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