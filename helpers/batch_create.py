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


def preload_businesses(data):
    for key, item in data.items():
        __building = item['building']
        __business = item['business']
        __address = item['address']
        __latitude = item['latitude']
        __longitude = item['longitude']

        try:
            building = Building.objects.get(name=__building)
        except Building.DoesNotExist:
            building = create_building(item)

        try:
            business = Business.objects.get(name=__business)
        except Business.DoesNotExist:
            fixture = AutoFixture(
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

            business = fixture.create(1)

        print(f"{business} created in {building}")


def create_building(item):
    __building = item['building']
    __address = item['address']
    __latitude = item['latitude']
    __longitude = item['longitude']
    height = round(random.uniform(25, 300), 2)
    floors = int(height // 4.25)
    floor_area = round(random.uniform(80, 600), 2)
    total_floor_area = floor_area * floors
    field_values = {
        'name': __building,
        'address': __address,
        'region': region,
        'province': province,
        'city': city,
        'latitude': __latitude,
        'longitude': __longitude,
        'date_of_construction': DateDim.objects.filter(year__lt=2017).order_by('?').first().date_obj,
        'beams': random.randint(0, 6),
        'columns': random.randint(0, 6),
        'flooring': random.randint(0, 6),
        'exterior_walls': random.randint(0, 6),
        'corridor_walls': random.randint(0, 6),
        'room_partitions': random.randint(0, 6),
        'main_stair': random.randint(0, 6),
        'window': random.randint(0, 6),
        'ceiling': random.randint(0, 6),
        'main_door': random.randint(0, 6),
        'trusses': random.randint(0, 6),
        'roof': random.randint(0, 6),
        'height': height,
        'floor_number': floors,
        'floor_area': floor_area,
        'total_floor_area': total_floor_area
    }
    building = Building.objects.create(**field_values)
    return building


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


def incidents():
    day = DateDim.objects.last()
    while day:
        business = Business.objects.all().order_by('?').first()
        chance = incident_chance(business.building, day)
        prob = random.uniform(0, 1)
        print(f"{business}, {business.building} \n\t Date: {day}\t\t Chance: {chance}")
        if chance > prob:
            incident_detail(business=business, d=day)
        try:
            t = day.tomorrow()
            day = DateDim.objects.get(date_obj=t)
        except DateDim.DoesNotExist:
            day = False


def incident_chance(building: Building, d: DateDim):
    checklist = building.building_checklist.get(
        date_checked__year=d.year
    )

    chance_of_fire = checklist.risk()

    chance_of_fire += ((5 - building.avg_fire_rating()) / 5) * 0.1
    chance_of_fire += building.age_risk(d.date_obj)

    if 3 <= d.month <= 5:
        chance_of_fire += 0.1

    return chance_of_fire


def incident_detail(business: Business, d: DateDim):
    v = {
        'business': business,
        'building': business.building,
        'incident_type': 'Structural',
        'occurrence': d,
        'region': region,
        'province': province,
        'city': city
    }
    checklist = business.building.building_checklist.get(
        date_checked__year=d.year,
        business=business
    )

    if business.building.avg_fire_rating() < 2:
        damage_range = [5, 25]
        casualty_range = [0, .1]
        intensity_range = [1, 5]
        severity_range = [1, 6]
        duration_range = [30, 240]
        minor_injuries_range = [0, .1]
        major_injuries_range = [0, .2]
    elif business.building.avg_fire_rating() < 3:
        damage_range = [5, 60]
        casualty_range = [0, .15]
        intensity_range = [1, 7]
        severity_range = [1, 6]
        duration_range = [45, 340]
        minor_injuries_range = [0, .4]
        major_injuries_range = [0, .3]
    elif business.building.avg_fire_rating() < 4:
        damage_range = [12, 95]
        casualty_range = [0, .2]
        intensity_range = [1, 8]
        severity_range = [1, 8]
        duration_range = [60, 540]
        minor_injuries_range = [0, .5]
        major_injuries_range = [0, .4]
    else:
        damage_range = [30, 999]
        casualty_range = [0, .5]
        intensity_range = [2, 10]
        severity_range = [3, 10]
        duration_range = [60, 1940]
        minor_injuries_range = [0, .6]
        major_injuries_range = [0, .5]

    v['property_damage'] = random.uniform(damage_range[0], damage_range[1])
    v['casualties'] = random.uniform(casualty_range[0], casualty_range[1]) * checklist.heads_total_count
    v['major_injuries'] = random.uniform(major_injuries_range[0], major_injuries_range[1]) * checklist.heads_total_count
    v['minor_injuries'] = random.uniform(minor_injuries_range[0], minor_injuries_range[1]) * checklist.heads_total_count
    v['intensity'] = random.uniform(intensity_range[0], intensity_range[1])
    v['severity'] = random.uniform(severity_range[0], severity_range[1])
    v['duration'] = random.uniform(duration_range[0], duration_range[1])

    fixture = AutoFixture(
        Incident,
        field_values=v
    )

    fixture.create(1)
    print(f"{fixture} created")
