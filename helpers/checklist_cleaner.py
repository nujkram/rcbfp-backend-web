import random

from checklists.models.checklist.checklist_models import Checklist

policy_code = 'PN'
fsic_code = 'FS'
violation_code = 'VC'
electrical_code = 'EPN'

TERMINATION_OF_EXIT_CHOICES = [
    "None",
    "ok - discharge exit (front/back)",
    "ok - discharge exit (front)",
    "ok - discharge exit (back)",
]

EXIT_ENCLOSURE_CONSTRUCTION_CHOICES = [
     "Standard (Open Exit)",
     "Standard",
     "Standard Concrete",
]

EXIT_FIRE_DOOR_CONSTRUCTION_CHOICES = [
    "Standard (Glass door in front)",
    "Standard open exit in front and back",
    "Standard",
]

STAIRS_ENCLOSURE_CONSTRUCTION_CHOICES = [
    "Standard",
    "Standard Concrete",
    "Standard Wood",
]

STAIRS_FIRE_DOOR_CONSTRUCTION_CHOICES = [
    "Standard",
    "Standard Concrete",
    "Standard Wood",
]

CONTROL_PANEL_LOCATION_CHOICES = [
    "Stock Room",
    "Storage Room",
]

SMOKING_LOCATION_CHOICES = [
    "Back area",
    "Parking lot",
    "Outside",
]

STORAGE_LOCATION_CHOICES = [
    "Inside near counter",
    "Inside main floor",
    "Back area",
    "Back near kitchen",
    "Back near comfort room",
]

OVEN_USED_CHOICES = [
    "None",
    "Yes",
    "Yes - Electric Oven",
]

KIND_OF_FUEL_CHOICES = [
    "None",
    "LPG",
    "Electricity",
]


SMOKE_HOOD_CHOICES = [
    "None",
    "Yes",
]

SPARK_ARRESTER_CHOICES = [
    "None",
    "Yes",
]

PARTITION_CONSTRUCTION_CHOICES = [
    "None",
    "Standard",
]

NOTES_CHOICES = [
    "None",
    "Lacking of requirements",
    "Comply inspection requirements",
    "No fire alarm and no smoking sign",
]

RECOMMENDATION_CHOICES = [
    "None",
    "Immediate compliance",
]


def clean_checklists(checklists):
    policy_int = random.randint(100000, 999999)
    fsic_int = random.randint(100000, 999999)
    violation_int = random.randint(100000, 999999)
    electrical_int = random.randint(100000, 999999)

    policy_no = f"{policy_code}{policy_int}"
    fsic_control_no = f"{fsic_code}{fsic_int}"
    violation_control_no = f"{violation_code}{violation_int}"
    electrical_inspection_no = f"{electrical_code}{electrical_int}"

    for checklist in checklists:
        checklist.first_name = checklist.business.owner_first_name
        checklist.middle_name = checklist.business.owner_middle_name
        checklist.last_name = checklist.business.owner_last_name
        checklist.policy_no = policy_no
        checklist.fsic_control_no = fsic_control_no
        checklist.violation_control_no = violation_control_no
        checklist.electrical_inspection_no = electrical_inspection_no
        x = random.randint(0, 3)
        checklist.termination_of_exit = TERMINATION_OF_EXIT_CHOICES[x]
        x = random.randint(0, 2)
        checklist.exits_enclosure_construction = EXIT_ENCLOSURE_CONSTRUCTION_CHOICES[x]
        x = random.randint(0, 2)
        checklist.exits_fire_door_construction = EXIT_FIRE_DOOR_CONSTRUCTION_CHOICES[x]
        x = random.randint(0, 2)
        checklist.stairs_enclosure_construction = STAIRS_ENCLOSURE_CONSTRUCTION_CHOICES[x]
        x = random.randint(0, 2)
        checklist.stairs_fire_door_construction = STAIRS_FIRE_DOOR_CONSTRUCTION_CHOICES[x]
        x = random.randint(0, 1)
        checklist.control_panel_location = CONTROL_PANEL_LOCATION_CHOICES[x]
        x = random.randint(0, 2)
        checklist.smoking_area_location = SMOKING_LOCATION_CHOICES[x]
        x = random.randint(0, 4)
        checklist.storage_location = STORAGE_LOCATION_CHOICES[x]
        x = random.randint(0, 2)
        checklist.oven_used = OVEN_USED_CHOICES[x]
        if not x :
            checklist.kind_of_fuel = "None"
            checklist.smoke_hood = "None"
            checklist.spark_arrester = "None"
        else:
            x = random.randint(0, 1)
            checklist.kind_of_fuel = KIND_OF_FUEL_CHOICES[x]
            checklist.smoke_hood = SMOKE_HOOD_CHOICES[x]
            checklist.spark_arrester = SPARK_ARRESTER_CHOICES[x]

        x = random.randint(0, 1)
        checklist.partition_construction = PARTITION_CONSTRUCTION_CHOICES[x]
        x = random.randint(0, 3)
        checklist.notes = NOTES_CHOICES[x]

        if checklist.status != 0:
            checklist.recommendations = RECOMMENDATION_CHOICES[0]
        else:
            checklist.recommendations = RECOMMENDATION_CHOICES[1]

        checklist.save()
