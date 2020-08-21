from django.db import models
from django.apps import apps

from locations.models import Region, Province, City


class BuildingQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class BuildingManager(models.Manager):
    def get_queryset(self):
        return BuildingQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []

        try:
            region = Region.objects.get(name=kwargs['region'])
        except Region.DoesNotExist:
            flag = False
            m.append(f'{region} is an invalid region')

        try:
            province = Province.objects.get(name=kwargs['province'])
        except Province.DoesNotExist:
            flag = False
            m.append(f'{province} is an invalid province')

        try:
            city = City.objects.get(name=kwargs['city'])
        except City.DoesNotExist:
            flag = False
            m.append(f'{city} is an invalid city')

        if flag:
            building = self.model(
                name=kwargs['name'],
                address=kwargs['address'],
                latitude=kwargs['latitude'],
                longitude=kwargs['longitude'],
                date_of_construction=kwargs['date_of_construction'],
                floor_number=kwargs['floor_number'],
                height=kwargs['height'],
                floor_area=kwargs['floor_area'],
                total_floor_area=kwargs['total_floor_area'],
                beams=kwargs['beams'],
                columns=kwargs['columns'],
                flooring=kwargs['flooring'],
                exterior_walls=kwargs['exterior_walls'],
                corridor_walls=kwargs['corridor_walls'],
                room_partitions=kwargs['room_partitions'],
                main_stair=kwargs['main_stair'],
                window=kwargs['window'],
                ceiling=kwargs['ceiling'],
                main_door=kwargs['main_door'],
                trusses=kwargs['trusses'],
                roof=kwargs['roof'],
                entry_road_width=kwargs['entry_road_width'],
                region=kwargs['region'],
                province=kwargs['province'],
                city=kwargs['city'],
            )
            building.save()
            return building, 'Building recorded!'
        else:
            return False, m
