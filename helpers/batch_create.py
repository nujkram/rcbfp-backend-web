from autofixture import AutoFixture
import random
from django.core.exceptions import ObjectDoesNotExist

from buildings.models.building.building_models import Building
from business.models import Business
from checklists.models.checklist.checklist_models import Checklist
from datesdim.models import DateDim
from incidents.models.incident.incident_models import Incident, IncidentCoordinate
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

        building = Building.objects.get(name=__building)

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
        'total_floor_area': total_floor_area,
        'entry_road_width': random.randint(10, 25)
    }
    building = Building.objects.create(**field_values)
    return building


def checklists(businesses, checklist_year):
    print(f"Checklist year: {checklist_year}")
    counter = 0
    for business in businesses:
        print(f"Construction year for {business.building}: {business.building.date_of_construction.year}")
        if business.building.date_of_construction.year < checklist_year:
            print("creating...")
            year = checklist_year
            schedule = DateDim.objects.get_days_between(start=f'{year}-01-01', end=f'{year}-12-31')

            fixture = AutoFixture(
                Checklist,
                field_values={
                    'business': business,
                    'building': business.building,
                    'date_checked': random.choice(schedule),
                    'building_permit': 1,
                    'occupancy_permit': 1,
                    'fire_drill_certificate': 1,
                    'any_renovation': random.randint(0, 1),
                    'is_exits_remote': random.randint(0, 1),
                    'any_enclosure': random.randint(0, 1),
                    'is_exit_accessible': random.randint(0, 1),
                    'is_fire_doors_provided': random.randint(0, 1),
                    'self_closing_mechanism': random.randint(0, 1),
                    'panic_hardware': random.randint(0, 1),
                    'readily_accessible': random.randint(0, 1),
                    'travel_distance_within_limit': random.randint(0, 1),
                    'adequate_illumination': random.randint(0, 1),
                    'panic_hardware_operational': random.randint(0, 1),
                    'doors_open_easily': random.randint(0, 1),
                    'bldg_with_mezzanine': random.randint(0, 1),
                    'is_obstructed': random.randint(0, 1),
                    'dead_ends_within_limits': random.randint(0, 1),
                    'proper_rating_illumination': random.randint(0, 1),
                    'door_swing_in_the_direction_of_exit': random.randint(0, 1),
                    'self_closure_operational': random.randint(0, 1),
                    'mezzanine_with_proper_exits': random.randint(0, 1),
                    'corridors_of_sufficient_size': random.randint(0, 1),
                    'main_stair_railings': random.randint(0, 1),
                    'main_stair_any_enclosure_provided': random.randint(0, 1),
                    'any_openings': random.randint(0, 1),
                    'main_stair_door_proper_rating': random.randint(0, 1),
                    'main_stair_door_provided_with_vision_panel': random.randint(0, 1),
                    'main_stair_pressurized_stairway': random.randint(0, 1),
                    'fire_escape_railings': random.randint(0, 1),
                    'fire_escape_obstruction': random.randint(0, 1),
                    'discharge_of_exits': random.randint(0, 1),
                    'fire_escape_enclosure': random.randint(0, 1),
                    'fire_escape_opening': random.randint(0, 1),
                    'fire_escape_opening_protected': random.randint(0, 1),
                    'fire_door_provided': random.randint(0, 1),
                    'fire_door_door_proper_rating': random.randint(0, 1),
                    'fire_door_door_provided_with_vision_panel': random.randint(0, 1),
                    'fire_door_pressurized_stairway': random.randint(0, 1),
                    'horizontal_exit_vision_panel': random.randint(0, 1),
                    'horizontal_exit_door_swing_in_direction_of_egress': random.randint(0, 1),
                    'horizontal_exit_with_self_closing_device': random.randint(0, 1),
                    'horizontal_exit_corridor_walls_extended': random.randint(0, 1),
                    'horizontal_exit_properly_illuminated': random.randint(0, 1),
                    'horizontal_exit_readily_visible': random.randint(0, 1),
                    'horizontal_exit_properly_marked': random.randint(0, 1),
                    'horizontal_exit_with_illuminated_directional_sign': random.randint(0, 1),
                    'horizontal_exit_properly_located': random.randint(0, 1),
                    'ramps_provided': random.randint(0, 1),
                    'ramps_railing_provided': random.randint(0, 1),
                    'ramps_enclosure': random.randint(0, 1),
                    'ramps_fire_doors': random.randint(0, 1),
                    'ramps_with_self_closing_device': random.randint(0, 1),
                    'ramps_door_with_proper_rating': random.randint(0, 1),
                    'ramps_door_with_vision_panel': random.randint(0, 1),
                    'ramps_door_swing_in_direction_of_egress': random.randint(0, 1),
                    'ramps_obstruction': random.randint(0, 1),
                    'ramps_discharge_of_exit': random.randint(0, 1),
                    'safe_refuge_provided': random.randint(0, 1),
                    'safe_refuge_enclosure': random.randint(0, 1),
                    'safe_refuge_fire_door': random.randint(0, 1),
                    'safe_refuge_with_self_closing_device': random.randint(0, 1),
                    'safe_refuge_door_proper_rating': random.randint(0, 1),
                    'safe_refuge_with_vision_panel': random.randint(0, 1),
                    'safe_refuge_vision_panel_built': random.randint(0, 1),
                    'safe_refuge_swing_in_direction_of_egress': random.randint(0, 1),
                    'emergency_light': random.randint(0, 1),
                    'emergency_light_operational': random.randint(0, 1),
                    'emergency_light_exit_path_properly_illuminated': random.randint(0, 1),
                    'emergency_light_tested_monthly': random.randint(0, 1),
                    'exit_signs_illuminated': random.randint(0, 1),
                    'exit_signs_visible': random.randint(0, 1),
                    'exit_route_posted_on_lobby': random.randint(0, 1),
                    'exit_route_posted_on_rooms': random.randint(0, 1),
                    'directional_exit_signs': random.randint(0, 1),
                    'no_smoking_sign': random.randint(0, 1),
                    'dead_end_sign': random.randint(0, 1),
                    'elevator_sign': random.randint(0, 1),
                    'keep_door_closed_sign': random.randint(0, 1),
                    'vertical_openings_properly_protected': random.randint(0, 1),
                    'vertical_openings_atrium': random.randint(0, 1),
                    'fire_doors_good_condition': random.randint(0, 1),
                    'elevator_opening_protected': random.randint(0, 1),
                    'pipe_chase_opening_protected': random.randint(0, 1),
                    'aircon_ducts_with_dumper': random.randint(0, 1),
                    'garbage_chute_protected': random.randint(0, 1),
                    'between_floor_protected': random.randint(0, 1),
                    'siamese_intake_provided': random.randint(0, 1),
                    'siamese_intake_accessible': random.randint(0, 1),
                    'fire_hose_cabinet': random.randint(0, 1),
                    'fire_hose_cabinet_accessories': random.randint(0, 1),
                    'fire_lane': random.randint(0, 1),
                    'portable_fire_extinguisher_with_ps_mark': random.randint(0, 1),
                    'portable_fire_extinguisher_with_iso_mark': random.randint(0, 1),
                    'portable_fire_extinguisher_maintained': random.randint(0, 1),
                    'portable_fire_extinguisher_accessible': random.randint(0, 1),
                    'sprinkler_system_agent_used': random.randint(0, 1),
                    'maintaining_line_pressure': random.randint(0, 1),
                    'plan_submitted': random.randint(0, 1),
                    'firewall_required': random.randint(0, 1),
                    'firewall_provided': random.randint(0, 1),
                    'firewall_opening': random.randint(0, 1),
                    'boiler_provided': random.randint(0, 1),
                    'lpg_installation_with_permit': random.randint(0, 1),
                    'fuel_with_storage_permit': random.randint(0, 1),
                    'generator_set': random.randint(0, 1),
                    'generator_bound_on_wall': random.randint(0, 1),
                    'generator_mechanical_permit': random.randint(0, 1),
                    'generator_fuel_storage_permit': random.randint(0, 1),
                    'generator_automatic_transfer_switch': random.randint(0, 1),
                    'refuse_handling': random.randint(0, 1),
                    'refuse_handling_enclosure': random.randint(0, 1),
                    'refuse_handling_fire_resistive': random.randint(0, 1),
                    'refuse_handling_fire_protection': random.randint(0, 1),
                    'refuse_handling_disposal': random.randint(0, 1),
                    'electrical_hazard': random.randint(0, 1),
                    'mechanical_hazard': random.randint(0, 1),
                    'fireman_elevator': random.randint(0, 1),
                    'fireman_elevator_key': random.randint(0, 1),
                    'separation_fire_rated': random.randint(0, 1),
                    'separation_fire_rated_accessible': random.randint(0, 1),
                    'separation_fire_rated_fuel': random.randint(0, 1),
                    'separation_fire_rated_permit': random.randint(0, 1),
                    'chimney_spark_arrestor': random.randint(0, 1),
                    'chimney_smoke_hood': random.randint(0, 1),
                    'hazardous_material': random.randint(0, 1),
                    'hazardous_material_stored': random.randint(0, 1),
                    'fire_brigade_organization': random.randint(0, 1),
                    'fire_safety_seminar': random.randint(0, 1),
                    'employee_trained_in_emergency_procedures': random.randint(0, 1),
                    'evacuation_drill_first': random.randint(0, 1),
                    'evacuation_drill_second': random.randint(0, 1),
                },
                none_p=None
            )

            fixture.create(1)
            business.is_safe()
            counter += 1
        else:
            pass

    return print(f'({counter}) checklists created')


def incidents():
    day = DateDim.objects.last()
    while day:
        business = Business.objects.filter(building__date_of_construction__lt=str(day)).order_by('?').first()
        if business:
            try:
                chance = incident_chance(business.building, day)
                prob = random.uniform(0, 1)
                print(f"{business}, {business.building} \n\t Date: {day}\t\t Chance: {chance}")
                if chance > prob:
                    incident_detail(business=business, d=day)
            except ObjectDoesNotExist:
                print(f"{business}: {business.building} has no checklist on {day}")
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
