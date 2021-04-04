from django.db import models
from django.apps import apps

from datesdim.models import DateDim


class ChecklistQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class ChecklistManager(models.Manager):
    def get_queryset(self):
        return ChecklistQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []
        date_value = kwargs['date_checked']
        try:
            checked_date = DateDim.objects.get(year=date_value.year, month=date_value.month, day=date_value.day)
        except DateDim.DoesNotExist:
            flag = False
            m.append(f'{DateDim} is an invalid building')

        if kwargs['policy_no']:
            policy_no = kwargs['policy_no']
        else:
            policy_no = 0

        if kwargs['building_permit']:
            building_permit = kwargs['building_permit']
        else:
            building_permit = 0

        if kwargs['occupancy_permit']:
            occupancy_permit = kwargs['occupancy_permit']
        else:
            occupancy_permit = 0

        if kwargs['fsic_control_no']:
            fsic_control_no = kwargs['fsic_control_no']
        else:
            fsic_control_no = 0

        if kwargs['fsic_fee']:
            fsic_fee = kwargs['fsic_fee']
        else:
            fsic_fee = 0

        if kwargs['fire_drill_certificate']:
            fire_drill_certificate = kwargs['fire_drill_certificate']
        else:
            fire_drill_certificate = 0

        if kwargs['violation_control_no']:
            violation_control_no = kwargs['violation_control_no']
        else:
            violation_control_no = 0

        if kwargs['electrical_inspection_no']:
            electrical_inspection_no = kwargs['electrical_inspection_no']
        else:
            electrical_inspection_no = 0

        if kwargs['sectional_occupancy']:
            sectional_occupancy = kwargs['sectional_occupancy']
        else:
            sectional_occupancy = 0

        if kwargs['exits_count']:
            exits_count = kwargs['exits_count']
        else:
            exits_count = 0

        if kwargs['exits_width']:
            exits_width = kwargs['exits_width']
        else:
            exits_width = 0

        if kwargs['exits_accessible']:
            exits_accessible = kwargs['exits_accessible']
        else:
            exits_accessible = 0

        if kwargs['termination_of_exit']:
            termination_of_exit = kwargs['termination_of_exit']
        else:
            termination_of_exit = 0

        if kwargs['exits_enclosure_provided']:
            exits_enclosure_provided = kwargs['exits_enclosure_provided']
        else:
            exits_enclosure_provided = 0

        if kwargs['exits_enclosure_construction']:
            exits_enclosure_construction = kwargs['exits_enclosure_construction']
        else:
            exits_enclosure_construction = 0

        if kwargs['exits_fire_doors_provided']:
            exits_fire_doors_provided = kwargs['exits_fire_doors_provided']
        else:
            exits_fire_doors_provided = 0

        if kwargs['exits_fire_door_construction']:
            exits_fire_door_construction = kwargs['exits_fire_door_construction']
        else:
            exits_fire_door_construction = 0

        if kwargs['stairs_count']:
            stairs_count = kwargs['stairs_count']
        else:
            stairs_count = 0

        if kwargs['stairs_enclosure_provided']:
            stairs_enclosure_provided = kwargs['stairs_enclosure_provided']
        else:
            stairs_enclosure_provided = 0

        if kwargs['stairs_enclosure_construction']:
            stairs_enclosure_construction = kwargs['stairs_enclosure_construction']
        else:
            stairs_enclosure_construction = 0

        if kwargs['stairs_fire_doors_provided']:
            stairs_fire_doors_provided = kwargs['stairs_fire_doors_provided']
        else:
            stairs_fire_doors_provided = 0

        if kwargs['stairs_fire_door_construction']:
            stairs_fire_door_construction = kwargs['stairs_fire_door_construction']
        else:
            stairs_fire_door_construction = 0

        if kwargs['other_details']:
            other_details = kwargs['other_details']
        else:
            other_details = 0

        if kwargs['emergency_light']:
            emergency_light = kwargs['emergency_light']
        else:
            emergency_light = 0

        if kwargs['exit_signs_illuminated']:
            exit_signs_illuminated = kwargs['exit_signs_illuminated']
        else:
            exit_signs_illuminated = 0

        if kwargs['fire_extinguisher_count']:
            fire_extinguisher_count = kwargs['fire_extinguisher_count']
        else:
            fire_extinguisher_count = 0

        if kwargs['fire_extinguisher_accessible']:
            fire_extinguisher_accessible = kwargs['fire_extinguisher_accessible']
        else:
            fire_extinguisher_accessible = 0

        if kwargs['fire_extinguisher_conspicuous_location']:
            fire_extinguisher_conspicuous_location = kwargs['fire_extinguisher_conspicuous_location']
        else:
            fire_extinguisher_conspicuous_location = 0

        if kwargs['fire_alarm']:
            fire_alarm = kwargs['fire_alarm']
        else:
            fire_alarm = 0

        if kwargs['detectors']:
            detectors = kwargs['detectors']
        else:
            detectors = 0

        if kwargs['control_panel_location']:
            control_panel_location = kwargs['control_panel_location']
        else:
            control_panel_location = 0

        if kwargs['control_panel_functional']:
            control_panel_functional = kwargs['control_panel_functional']
        else:
            control_panel_functional = 0

        if kwargs['hazardous_materials']:
            hazardous_materials = kwargs['hazardous_materials']
        else:
            hazardous_materials = 0

        if kwargs['hazardous_materials_properly_stored']:
            hazardous_materials_properly_stored = kwargs['hazardous_materials_properly_stored']
        else:
            hazardous_materials_properly_stored = 0

        if kwargs['no_smoking_sign']:
            no_smoking_sign = kwargs['no_smoking_sign']
        else:
            no_smoking_sign = 0

        if kwargs['smoking_permitted']:
            smoking_permitted = kwargs['smoking_permitted']
        else:
            smoking_permitted = 0

        if kwargs['smoking_area_location']:
            smoking_area_location = kwargs['smoking_area_location']
        else:
            smoking_area_location = 0

        if kwargs['storage_location']:
            storage_location = kwargs['storage_location']
        else:
            storage_location = 0

        if kwargs['safety_device_for_lpg']:
            safety_device_for_lpg = kwargs['safety_device_for_lpg']
        else:
            safety_device_for_lpg = 0

        if kwargs['oven_used']:
            oven_used = kwargs['oven_used']
        else:
            oven_used = 0

        if kwargs['kind_of_fuel']:
            kind_of_fuel = kwargs['kind_of_fuel']
        else:
            kind_of_fuel = 0

        if kwargs['smoke_hood']:
            smoke_hood = kwargs['smoke_hood']
        else:
            smoke_hood = 0

        if kwargs['spark_arrester']:
            spark_arrester = kwargs['spark_arrester']
        else:
            spark_arrester = 0

        if kwargs['partition_construction']:
            partition_construction = kwargs['partition_construction']
        else:
            partition_construction = 0


        if kwargs['defects']:
            defects = kwargs['defects']
        else:
            defects = 0

        if kwargs['recommendations']:
            recommendations = kwargs['recommendations']
        else:
            recommendations = 0

        if kwargs['notes']:
            notes = kwargs['notes']
        else:
            notes = 0

        if kwargs['building']:
            building = kwargs['building']
        else:
            building = 0

        if kwargs['business']:
            business = kwargs['business']
        else:
            business = 0

        if kwargs['building_permit_date_issued']:
            building_permit_date_issued = kwargs['building_permit_date_issued']
        else:
            building_permit_date_issued = None

        if kwargs['occupancy_permit_date_issued']:
            occupancy_permit_date_issued = kwargs['occupancy_permit_date_issued']
        else:
            occupancy_permit_date_issued = None

        if kwargs['fsic_date_issued']:
            fsic_date_issued = kwargs['fsic_date_issued']
        else:
            fsic_date_issued = None

        if kwargs['fire_drill_certificate_date_issued']:
            fire_drill_certificate_date_issued = kwargs['fire_drill_certificate_date_issued']
        else:
            fire_drill_certificate_date_issued = None

        if kwargs['violation_control_no_date_issued']:
            violation_control_no_date_issued = kwargs['violation_control_no_date_issued']
        else:
            violation_control_no_date_issued = None

        if kwargs['electrical_inspection_date_issued']:
            electrical_inspection_date_issued = kwargs['electrical_inspection_date_issued']
        else:
            electrical_inspection_date_issued = None

        if kwargs['insurance_date_issued']:
            insurance_date_issued = kwargs['insurance_date_issued']
        else:
            insurance_date_issued = None

        if flag:
            checklist = self.model(
                first_name=kwargs['first_name'],
                middle_name=kwargs['middle_name'],
                last_name=kwargs['last_name'],
                policy_no=policy_no,
                building_permit=building_permit,
                occupancy_permit=occupancy_permit,
                fsic_control_no=fsic_control_no,
                fsic_fee=fsic_fee,
                fire_drill_certificate=fire_drill_certificate,
                violation_control_no=violation_control_no,
                electrical_inspection_no=electrical_inspection_no,
                sectional_occupancy=sectional_occupancy,
                exits_count=exits_count,
                exits_width=exits_width,
                exits_accessible=exits_accessible,
                termination_of_exit=termination_of_exit,
                exits_enclosure_provided=exits_enclosure_provided,
                exits_enclosure_construction=exits_enclosure_construction,
                exits_fire_doors_provided=exits_fire_doors_provided,
                exits_fire_door_construction=exits_fire_door_construction,
                stairs_count=stairs_count,
                stairs_enclosure_provided=stairs_enclosure_provided,
                stairs_enclosure_construction=stairs_enclosure_construction,
                stairs_fire_doors_provided=stairs_fire_doors_provided,
                stairs_fire_door_construction=stairs_fire_door_construction,
                other_details=other_details,
                emergency_light=emergency_light,
                exit_signs_illuminated=exit_signs_illuminated,
                fire_extinguisher_count=fire_extinguisher_count,
                fire_extinguisher_accessible=fire_extinguisher_accessible,
                fire_extinguisher_conspicuous_location=fire_extinguisher_conspicuous_location,
                fire_alarm=fire_alarm,
                detectors=detectors,
                control_panel_location=control_panel_location,
                control_panel_functional=control_panel_functional,
                hazardous_materials=hazardous_materials,
                hazardous_materials_properly_stored=hazardous_materials_properly_stored,
                no_smoking_sign=no_smoking_sign,
                smoking_permitted=smoking_permitted,
                smoking_area_location=smoking_area_location,
                storage_location=storage_location,
                safety_device_for_lpg=safety_device_for_lpg,
                oven_used=oven_used,
                kind_of_fuel=kind_of_fuel,
                smoke_hood=smoke_hood,
                spark_arrester=spark_arrester,
                partition_construction=partition_construction,
                defects=defects,

                building_permit_date_issued=building_permit_date_issued,
                occupancy_permit_date_issued=occupancy_permit_date_issued,
                fsic_date_issued=fsic_date_issued,
                fire_drill_certificate_date_issued=fire_drill_certificate_date_issued,
                violation_control_no_date_issued=violation_control_no_date_issued,
                electrical_inspection_date_issued=electrical_inspection_date_issued,
                insurance_date_issued=insurance_date_issued,
                date_checked=checked_date,
                building=building,
                business=business,
                notes=notes,
                recommendations=recommendations,
            )

            checklist.save()
            return checklist, 'Checklist recorded!'
        else:
            return False, m
